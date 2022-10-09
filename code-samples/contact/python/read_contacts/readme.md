# Read Contacts

## Steps to test

- Install Nylas Python SDK

```
  pip install nylas
  pip install python-dotenv
```

- Setup ENV Variables

- Run the script

## Expected Output

A list of contact information as elements

```
[
  {
    'account_id': 'account-id',
    'api': <nylas.client.client.APIClient object at 0x1033a8e80>,
    'cls': <class 'nylas.client.restful_models.Contact'>,
    'company_name': 'company-name',
    'emails': defaultdict(<class 'list'>, {None: ['example@example.com']}),
    'given_name': 'Example',
    'id': 'exaMplE',
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
    'picture_url': None,
    'source': 'inbox',
    'suffix': None,
    'surname': None,
    'web_pages': defaultdict(<class 'list'>, {})},
  }
]
```
