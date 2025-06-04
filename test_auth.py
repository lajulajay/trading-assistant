from etrade_client.auth.oauth import ETradeAuth

def test_auth_flow():
    """Test the E*TRADE authentication flow."""
    try:
        # Initialize auth
        auth = ETradeAuth()
        
        # Authenticate (using sandbox by default)
        session, base_url = auth.authenticate(use_sandbox=True)
        
        print("Successfully authenticated!")
        print(f"Using base URL: {base_url}")
        return True
    except Exception as e:
        print(f"Authentication failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_auth_flow() 