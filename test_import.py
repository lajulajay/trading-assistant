from etrade_client.auth import ETradeAuth

def test_imports():
    print("Successfully imported ETradeAuth from etrade_client.auth")
    
    # Try to create an instance of ETradeAuth
    try:
        auth = ETradeAuth()
        print("\nSuccessfully created ETradeAuth instance")
    except Exception as e:
        print(f"\nError creating ETradeAuth instance: {e}")

if __name__ == "__main__":
    test_imports() 