"""Shared OAuth functionality for E*TRADE API authentication."""
import os
import configparser
from rauth import OAuth1Service
from dotenv import load_dotenv

class ETradeAuth:
    def __init__(self, config_path=None):
        """
        Initialize E*TRADE authentication.
        
        Args:
            config_path (str, optional): Path to config.ini. If None, looks in current directory.
        """
        self.config = configparser.ConfigParser()
        if config_path:
            self.config.read(config_path)
        else:
            self.config.read('config.ini')
        
        # Load environment variables as fallback
        load_dotenv()
        
        # Get credentials from config or environment
        self.consumer_key = self.config.get('DEFAULT', 'CONSUMER_KEY', fallback=os.getenv('ETRADE_CONSUMER_KEY'))
        self.consumer_secret = self.config.get('DEFAULT', 'CONSUMER_SECRET', fallback=os.getenv('ETRADE_CONSUMER_SECRET'))
        self.sandbox_url = self.config.get('DEFAULT', 'SANDBOX_BASE_URL', fallback='https://apisb.etrade.com')
        self.prod_url = self.config.get('DEFAULT', 'PROD_BASE_URL', fallback='https://api.etrade.com')

    def get_oauth_service(self, use_sandbox=True):
        """Get OAuth1Service instance for E*TRADE API."""
        base_url = self.sandbox_url if use_sandbox else self.prod_url
        
        return OAuth1Service(
            name="etrade",
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            request_token_url=f"{base_url}/oauth/request_token",
            access_token_url=f"{base_url}/oauth/access_token",
            authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
            base_url=base_url
        )

    def authenticate(self, use_sandbox=True):
        """
        Perform OAuth authentication flow.
        
        Args:
            use_sandbox (bool): Whether to use sandbox environment
            
        Returns:
            tuple: (session, base_url) where session is an authenticated OAuth session
        """
        etrade = self.get_oauth_service(use_sandbox)
        base_url = self.sandbox_url if use_sandbox else self.prod_url

        # Get request token
        request_token, request_token_secret = etrade.get_request_token(
            params={"oauth_callback": "oob", "format": "json"}
        )

        # Get authorization URL and open in browser
        authorize_url = etrade.authorize_url.format(etrade.consumer_key, request_token)
        print(f"Please visit this URL to authorize the application: {authorize_url}")
        verification_code = input("Enter the verification code from the browser: ")

        # Get access token
        session = etrade.get_auth_session(
            request_token,
            request_token_secret,
            params={"oauth_verifier": verification_code}
        )

        return session, base_url 