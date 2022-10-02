# Prerequisites

 - install Nylas using the command `pip install nylas` 
 - [optional] if required install `pip install python-dotenv` 
 - Sync and generate `CLIENT_ID, CLIENT_SECRET and ACCESS_TOKEN` from Nylas Dashboard for the email account you want to process. 
 - Update the values in these 3 lines mentioned below : 

    `os.environ['CLIENT_ID'] = "The ID for your application"
os.environ['CLIENT_SECRET'] = "The secret for your application"
os.environ['ACCESS_TOKEN'] = "The access token you generated with the Quick Start application."`
