# Read Account using Python SDK

## Setup

1) In the root folder, create a .env file with your nylas configuration as follow

```bash
  CLIENT_ID="YOUR_CLIENT_ID"
  CLIENT_SECRET="YOUR_CLIENT_SECRET"
  ACCOUNT_ID="YOUR_ACCOUNT_ID"
```

1) Install dependencies

```bash
  python -m pip install nylas dotenv
```

## Usage

Run the script using the npm:

```bash
  python main.py
```

## Output

```bash
  Account ID: account_id
  Email: your-mail@provider.app      
  Provider: provider_name
```
