import os
from nylas import APIClient

### Add the client credentials to the environment variables
nylas = APIClient(
   os.environ.get("CLIENT_ID"),
   os.environ.get("CLIENT_SECRET"),
   os.environ.get("ACCESS_TOKEN"),
)
 
### Get All Contacts
contacts = nylas.contacts.all()
print(contacts)

### Get Individual Contact
contact = nylas.contacts.get('ID')  # Provide contact ID as the argument
print(contact)
