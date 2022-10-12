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


# Create Contact Using Nylas SDK 

contact = nylas.contacts.create()
contact.given_name = "Anonymous"
contact.middle_name = "Frog"
contact.surname = "Tanuki"
contact.emails['personal'] = ['ytafkocjc@laste.ml']
contact.notes = "Test Contact - Kuro"
contact.phone_numbers['personal'] = ['(555) 867-5309']
contact.web_pages['homepage'] = ['https://nylas.com']
contact.save()
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(contact)

#fetch the ID of the newly created contact. 
new_contact_id = contact.id 

# Read newly created contact
contact = nylas.contacts.get(new_contact_id)
pp_contact = pprint.PrettyPrinter(indent=4)
print("********** Below are the details of the new Contact Created **********")
pp_contact.pprint(contact)