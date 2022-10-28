# Re-occuring Calendar Event using Nylas Python SDK

  

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

  

Update the `.env` file with the desired Calendar ID to fetch events from: 

  

```bash

CALENDAR_ID = "YOUR_CALENDAR_ID"
EMAIL_TO = "RECEPIENT_EMAIL"

```

  

## Output

  

When the calendar is successfully created we will get below output:

  

```text
Event created successfully! See you Soon. 
Recurring event is generated successfully!
Desired invitee's are present.

```

Additionally, you can also Manually verify if a recurring event is available on your and the invitee's calendar as well. 