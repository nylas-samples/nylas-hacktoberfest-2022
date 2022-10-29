
# Filter Emails with Python Nylas SDK

  

  

## Setup

  

  

1) Update below values in your `.env` file.

  

  

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

  

Execute the python files using command line or in any editor of your choice ensuring python is setup. 

Ensure to update your keyword of choice to search for in the variable: 
```
# Keyword to search under subject
subject_to_search =  'unsubscribe'
```
  

## Output


Sample output of execution :
 
```bash
Re: [nylas-samples/nylas-hacktoberfest-2022] Using the Nylas Python SDK, list last 10 emails that contain a keyword, like 'unsubscribe' (Issue #67)
Re: [nylas-samples/nylas-hacktoberfest-2022] Using the Nylas Python SDK, list last 10 emails that contain a keyword, like 'unsubscribe' (Issue #67)
```