# Create an account with Python Nylas SDK

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
Sample output of execution : 
{   'account_id': '2fxrlrbxi544wxkkum3atk1dh',
    'api': <nylas.client.client.APIClient object at 0x7f7fcfbb52e0>,
    'cls': <class 'nylas.client.restful_models.Contact'>,
    'company_name': None,
    'emails': defaultdict(<class 'list'>, {'other': ['grereg-admin@ets.org']}),
    'given_name': None,
    'id': '7h9xzwgg7161y25y64nqv2tw',
    'im_addresses': defaultdict(<class 'list'>, {}),
    'job_title': None,
    'manager_name': None,
    'middle_name': None,
    'nickname': None,
    'notes': None,
    'object': 'contact',
    'office_location': None,
    'phone_numbers': defaultdict(<class 'list'>, {}),
    'physical_addresses': defaultdict(<class 'list'>, {}),
    'picture_url': 'https://api.nylas.com/contacts/7h9xzwgg7161y25y64nqv2tw/picture',
    'source': 'address_book',
    'suffix': None,
    'surname': None,
    'web_pages': defaultdict(<class 'list'>, {})}
```