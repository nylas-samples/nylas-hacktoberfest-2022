# Creating Calendar using Python SDK

## Setup

1) In the root folder, create a .env file with your nylas configuration as follow

```bash
  CLIENT_ID="YOUR_CLIENT_ID"
  CLIENT_SECRET="YOUR_CLIENT_SECRET"
  ACCESS_TOKEN="YOUR_NYLAS_ACCESS_TOKEN"
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
  ID: "Calendar ID"
  Account: "Account ID"
  Name: "Calendar Name"
  Description: "Description of your new calendar"
  Location: "Location Description"
```
