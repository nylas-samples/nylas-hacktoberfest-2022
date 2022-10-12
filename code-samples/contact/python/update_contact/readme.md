#  Update an existing account with Python Nylas SDK


##  Setup


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


##  Usage
  
Execute the python files using command line or in any editor of your choice ensuring python is setup. Replace below variables in the python file :

```bash

os.environ['CLIENT_ID'] = "The ID for your application"
os.environ['CLIENT_SECRET'] = "The secret for your application"
os.environ['ACCESS_TOKEN'] = "The access token you generated with the Quick Start application.

```

## Output

```bash

Sample output of execution :

********** Below are the details of the new Contact details that are updated **********
{   'account_id': '2fxrlrbxi544wxkkum3atk1dh',
    'api': <nylas.client.client.APIClient object at 0x7fe9f9eae2b0>,
    'birthday': datetime.date(2014, 6, 1),
    'cls': <class 'nylas.client.restful_models.Contact'>,
    'company_name': 'Naruto',
    'emails': defaultdict(<class 'list'>,
                          {   'other': ['grereg-admin@ets.org'],
                              'personal': ['wxtivmdud@emlhub.com']}),
    'given_name': 'Toriko',
    'id': '7h9xzwgg7161y25y64nqv2tw',
    'im_addresses': defaultdict(<class 'list'>,
                                {   'gtalk': ['G', 'o', 'o', 'g', 'l', 'e']}),
    'job_title': 'Animator',
    'manager_name': '',
    'middle_name': 'Tokyo',
    'nickname': 'Otaku',
    'notes': 'I Love Anime!',
    'object': 'contact',
    'office_location': 'Japan',
    'phone_numbers': defaultdict(<class 'list'>,
                                 {   'business': ['555 555-5555']}),
    'physical_addresses': defaultdict(<class 'list'>,
                                      {   'work': [   {   'city': 'Tokyo',
                                                          'country': 'JP',
                                                          'format': 'structured',
                                                          'postal_code': '94102',
                                                          'secondary_address': None,
                                                          'state': 'AB',
                                                          'street_address': '12 '
                                                                            'Daijobu '
                                                                            'St, '
                                                                            '8th '
                                                                            'Floor',
                                                          'type': 'work'}]}),
    'picture_url': 'https://api.nylas.com/contacts/7h9xzwgg7161y25y64nqv2tw/picture',
    'source': 'address_book',
    'suffix': 'Shinigami',
    'surname': 'Ghoul',
    'web_pages': defaultdict(<class 'list'>,
                             {   'homepage': ['https://Google.com']})}
```