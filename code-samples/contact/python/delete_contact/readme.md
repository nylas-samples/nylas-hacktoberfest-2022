
# Delete an existing account with Python Nylas SDK

  

  

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

pip install python-dotenv

```

  
  

## Usage

  

Execute the python files using command line or in any editor of your choice ensuring python is setup. Update below values in your `.env` file.

  

```bash

CLIENT_ID, CLIENT_SECRET and ACCESS_TOKEN

```

## Pre-requisite

  

Please add the contact id from an existing contact in the `.env` file in the below format.

```

CONTACT_ID = <contact id>

```

Read the contact details and fetch a contact ID using the [read contacts code sample](https://github.com/nylas-samples/nylas-hacktoberfest-2022/tree/main/code-samples/contact/python/read_contacts)

  

## Output

  
  



Sample output of execution :

For successfule Deletion : 
```bash
The provided ID Exists in the Contact List. Going ahead with Deletion.....
ID is deleted sucessfully!!
```
In case the provided ID does not exist: 
```bash
The ID to be deleted does NOT Exist in the Contact List. Operation is unsuccessful!

```

  

## Note : Expected Errors

  

If you try to update a contact that was auto-created, you will receive the below error.

```

nylas.client.errors.NylasApiError: 400 Bad Request. Reason: <contact_id> is an auto-generated contact and this operation isnt supported for auto-generated contacts.. Nylas Error Type: api_error

```