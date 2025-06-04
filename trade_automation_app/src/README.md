# E*TRADE Options Trading Automation

An AI-powered automated trading system for managing covered calls and cash secured puts across multiple E*TRADE accounts.

## Features

- Automated options trading using E*TRADE's API
- Support for multiple trading accounts
- Covered calls and cash secured puts strategies
- Pre-trade validation and approval system
- Real-time monitoring and performance tracking
- Secure credential management
- Comprehensive logging and error handling

## Project Structure

```
etrade/
├── config/                 # Configuration files
│   ├── accounts.yaml      # Account configurations
│   └── strategies.yaml    # Trading strategy parameters
├── src/
│   ├── api/              # E*TRADE API integration
│   ├── strategies/       # Trading strategy implementations
│   ├── validation/       # Trade validation logic
│   ├── monitoring/       # System monitoring and logging
│   └── ui/              # User interface components
├── tests/                # Test suite
├── logs/                 # Application logs
└── credentials/          # Secure credential storage (gitignored)
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `config/accounts.yaml.template` to `config/accounts.yaml` and fill in your E*TRADE API credentials
5. Configure your trading strategies in `config/strategies.yaml`

## Configuration

### Account Configuration
Edit `config/accounts.yaml` to configure your E*TRADE accounts:
- API credentials
- Account numbers
- Trading limits
- Risk parameters

### Strategy Configuration
Edit `config/strategies.yaml` to define:
- Covered calls parameters
- Cash secured puts parameters
- Position sizing rules
- Entry/exit criteria

## Security

- API credentials are stored securely and never committed to version control
- All API communications are encrypted
- Trade validation requires explicit approval
- Comprehensive logging for audit trails

## Usage

1. Start the trading system:
   ```bash
   python src/main.py
   ```

2. Access the web interface at `http://localhost:8000`

3. Monitor trades and system status through the dashboard

## Development

- Follow PEP 8 style guide
- Write tests for new features
- Update documentation for changes
- Use pre-commit hooks for code quality

## License

MIT License - See LICENSE file for details

## Disclaimer

This software is for educational purposes only. Use at your own risk. The authors are not responsible for any financial losses incurred through the use of this software. 