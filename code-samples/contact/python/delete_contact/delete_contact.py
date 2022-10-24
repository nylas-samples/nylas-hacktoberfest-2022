import os, pprint
from nylas import APIClient
from datetime import datetime
from dotenv import load_dotenv


# load the env variables
load_dotenv()

# Fetch the client credentials from the environment variables
nylas = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN"),
)

# Get All Contacts
contacts = nylas.contacts.all()

# # Print all the contacts for reference. Uncomment to see all the available IDs. 
# pp_contact = pprint.PrettyPrinter(indent=4)
# print("********** All Contact IDs **********")
# # pp_contact.pprint(contacts)
# for val in contacts:
#     print(val.id)

# read the contact ID to update from the .env file
delete_contact_id = os.environ.get("CONTACT_ID")

# Iterate through the resultent contacts list and then verify if the contact id exists. If YES then delete and exit. If NO then print unsuccessful message.
for val in contacts:
    # print(val.id)
    if delete_contact_id == val.id: 
        print("The provided ID Exists in the Contact List. Going ahead with Deletion.....")
        nylas.contacts.delete(delete_contact_id)
        print("ID is deleted sucessfully!!")
        break
else: 
    print("The ID to be deleted does NOT Exist in the Contact List. Operation is unsuccessful!")
