# E*TRADE Project

This project contains two main components:
1. `etrade_client`: A shared library for E*TRADE API authentication and basic operations
2. `trade_automation_app`: An application for automated trading using the E*TRADE API

## Project Structure

```
Etrade/
├── etrade_client/           # Shared E*TRADE client library
│   ├── auth/               # Authentication module
│   │   ├── __init__.py
│   │   └── oauth.py       # Shared OAuth functionality
│   ├── etrade_python_client/  # Original E*TRADE client code
│   └── setup.py           # Package setup
│
├── trade_automation_app/       # Trading automation application
│   ├── src/               # Source code
│   │   ├── __init__.py
│   │   └── main.py       # Main automation logic
│   ├── tests/            # Test files
│   └── setup.py          # Package setup
│
├── config/                # Shared configuration
│   └── settings.ini      # API credentials and settings
│
├── requirements.txt       # Shared dependencies
└── README.md             # This file
```

## Setup

1. Create and activate a virtual environment:
```zsh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the shared E*TRADE client:
```zsh
cd etrade_client
pip install -e .
```

3. Install the trade automation app:
```zsh
cd ../trade_automation_app
pip install -e .
```

4. Configure your credentials:
   - Copy `config/settings.ini.example` to `config/settings.ini`
   - Add your E*TRADE API credentials to `config/settings.ini`

## Usage

### Testing Authentication
```zsh
python test_auth.py
```

### Running Trade Automation
```zsh
cd trade_automation_app
python src/trade_automation/main.py
```

## Development

- The `etrade_client` package provides shared authentication and API functionality
- The `trade_automation_app` package implements your trading strategies
- Both packages can be developed independently while sharing common code

## Notes

- Keep your API credentials secure and never commit them to version control
- Use the sandbox environment for testing
- The authentication flow follows OAuth 1.0a protocol 