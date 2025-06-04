"""E*TRADE Trade Automation App."""
from etrade_client.auth.oauth import ETradeAuth

class TradeAutomation:
    def __init__(self, use_sandbox=True):
        """Initialize trade automation with authentication."""
        self.auth = ETradeAuth()
        self.session, self.base_url = self.auth.authenticate(use_sandbox=use_sandbox)
    
    def run(self):
        """Run the trading automation."""
        # Your trading logic here
        print(f"Connected to E*TRADE API at {self.base_url}")
        # Example: Get account list, place orders, etc.

def main():
    """Main entry point for trade automation."""
    try:
        # Initialize with sandbox by default
        automation = TradeAutomation(use_sandbox=True)
        automation.run()
    except Exception as e:
        print(f"Error running trade automation: {str(e)}")

if __name__ == "__main__":
    main() 