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

********** Below are the details of the new Contact Created **********
{   'account_id': '2fxrlrbxi544wxkkum3atk1dh',
    'api': <nylas.client.client.APIClient object at 0x7fb3266c92e0>,
    'cls': <class 'nylas.client.restful_models.Contact'>,
    'company_name': None,
    'emails': defaultdict(<class 'list'>, {'personal': ['ytafkocjc@laste.ml']}),
    'given_name': 'Anonymous',
    'id': '6fexq8ds96ws0i87a3klrl8e5',
    'im_addresses': defaultdict(<class 'list'>, {}),
    'job_title': None,
    'manager_name': None,
    'middle_name': 'Frog',
    'nickname': None,
    'notes': 'Test Contact - Kuro',
    'object': 'contact',
    'office_location': None,
    'phone_numbers': defaultdict(<class 'list'>,
                                 {   'personal': ['(555) 867-5309']}),
    'physical_addresses': defaultdict(<class 'list'>, {}),
    'picture_url': None,
    'source': 'address_book',
    'suffix': None,
    'surname': 'Tanuki',
    'web_pages': defaultdict(<class 'list'>,
                             {   'homepage': ['https://nylas.com']})}

```