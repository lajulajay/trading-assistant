"""Shared OAuth functionality for E*TRADE API authentication."""
import os
import configparser
from rauth import OAuth1Service
from dotenv import load_dotenv

class ETradeAuth:
    def __init__(self, config_path=None):
        """
        Initialize E*TRADE authentication.
        """
        # Load environment variables first
        load_dotenv()
        # Initialize config parser as fallback (for legacy support, can be removed if not needed)
        self.config = configparser.ConfigParser()
        # Get credentials from environment first, then fallback to config
        self.consumer_key = os.getenv('ETRADE_CONSUMER_KEY') or self.config.get('DEFAULT', 'CONSUMER_KEY', fallback=None)
        self.consumer_secret = os.getenv('ETRADE_CONSUMER_SECRET') or self.config.get('DEFAULT', 'CONSUMER_SECRET', fallback=None)
        self.sandbox_url = os.getenv('ETRADE_SANDBOX_URL', 'https://apisb.etrade.com')
        self.prod_url = os.getenv('ETRADE_PROD_URL', 'https://api.etrade.com')
        self.use_sandbox = os.getenv('ETRADE_USE_SANDBOX', 'true').lower() == 'true'

        if not self.consumer_key or not self.consumer_secret:
            raise ValueError("E*TRADE API credentials not found. Please set ETRADE_CONSUMER_KEY and ETRADE_CONSUMER_SECRET environment variables.")

    def get_oauth_service(self, use_sandbox=None):
        """Get OAuth1Service instance for E*TRADE API."""
        if use_sandbox is None:
            use_sandbox = self.use_sandbox
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