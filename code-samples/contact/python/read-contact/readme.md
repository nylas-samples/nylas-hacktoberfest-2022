# Reading Account with Python Nylas SDK

## Setup

1) Sync and generate `CLIENT_ID, CLIENT_SECRET and ACCESS_TOKEN` from Nylas Dashboard for the email account you want to process

```bash
  CLIENT_ID=""
  CLIENT_SECRET=""
  ACCOUNT_ID=""
```

1) Install dependencies

```bash
  pip install nylas
```

## Usage

Execute the python files using command line or in any editor of your choice ensuring python is setup. Replace below variables in the python file :

```bash
os.environ['CLIENT_ID'] = "The ID for your application"
os.environ['CLIENT_SECRET'] = "The secret for your application"
os.environ['ACCESS_TOKEN'] = "The access token you generated with the Quick Start application.
```

## Output

```bash
JSON object containing all the parameters of the contact. 
```