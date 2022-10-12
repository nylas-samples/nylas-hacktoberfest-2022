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
#pp.pprint(contact)

new_contact_id = pp.pprint(contact.id)

# Read newly created contact
contact = nylas.contacts.get(new_contact_id)
pp_contact = pprint.PrettyPrinter(indent=4)
pp_contact.pprint(contact)

# ----- Update / modify an existing contact 
contact.given_name = 'Toriko'
contact.middle_name = 'Tokyo'
contact.surname = 'Ghoul'
contact.suffix = 'Shinigami'
contact.nickname = 'Otaku'
contact.office_location = 'Japan'
contact.company_name = 'Naruto'
contact.notes = 'I Love Anime!'
contact.manager_name = ''
contact.job_title = 'Animator'
contact.birthday = datetime(2014, 6, 1)
contact.emails['personal'] = ['wxtivmdud@emlhub.com']
contact.physical_addresses['work'] = [{
   # physical addresses must be structured like the following
   'format': 'structured',
   'city': 'Tokyo',
   'country': 'JP',
   'state': 'AB',
   'postal_code': '94102',
   'type': 'work',
   'street_address': '12 Daijobu St, 8th Floor'}]
contact.phone_numbers['business'] = ['555 555-5555']
contact.web_pages['homepage'] = ['https://Google.com']
contact.im_addresses['gtalk'] = 'Google'

# Save the contact to Nylas with the updated configurtations
contact.save()

contact = nylas.contacts.get(new_contact_id)
pp_contact = pprint.PrettyPrinter(indent=4)
print("********** Below are the details of the new Contact details that are updated **********")
pp_contact.pprint(contact)
