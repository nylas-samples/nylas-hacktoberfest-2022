# from dotenv import load_dotenv
# load_dotenv()
 
import os, pprint
from nylas import APIClient

# Set environment variables
os.environ['CLIENT_ID'] = "The ID for your application"
os.environ['CLIENT_SECRET'] = "The secret for your application"
os.environ['ACCESS_TOKEN'] = "The access token you generated with the Quick Start application."

nylas = APIClient(
   os.environ.get("CLIENT_ID"),
   os.environ.get("CLIENT_SECRET"),
   os.environ.get("ACCESS_TOKEN"),
)
 
## Read All contacts 
contact = nylas.contacts.all()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(contact)

# Read Individual contacts -  fetching for ID : 'ecmgrk86223gcvphwouglfuov' 
contact = nylas.contacts.get('ecmgrk86223gcvphwouglfuov')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(contact)