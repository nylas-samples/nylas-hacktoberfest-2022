import os, pprint
from nylas import APIClient
from datetime import datetime

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
#pp.pprint(contact)

new_contact_id = pp.pprint(contact.id)

# Read newly created contact
contact = nylas.contacts.get(new_contact_id)
pp_contact = pprint.PrettyPrinter(indent=4)
pp_contact.pprint(contact)


# ----- Update / modify an existing contact 

# The following attributes can be modified for the contact object
contact.given_name = 'Toriko'
contact.middle_name = 'Tokyo'
contact.surname = 'Ghoul'
contact.suffix = ''
contact.nickname = 'Otaku'
contact.office_location = 'Japan'
contact.company_name = 'Naruto'
contact.notes = 'I Love Anime!'
contact.manager_name = ''
contact.job_title = 'Animator'
contact.birthday = datetime(2014, 6, 1)
# emails must be one of type personal, or work
contact.emails['personal'] = ['wxtivmdud@emlhub.com']
# physical_addresses must be one of type work, home, or other
contact.physical_addresses['work'] = [{
   # physical addresses must be structured like the following
   'format': 'structured',
   'city': 'Tokyo',
   'country': 'JP',
   'state': 'AB',
   'postal_code': '94102',
   'type': 'work',
   'street_address': '12 Daijobu St, 8th Floor'}]
# phone_numbers must be one of type
# business, organization_main, mobile, assistant,
# business_fax, home_fax, radio, car, home, or pager
contact.phone_numbers['business'] = ['555 555-5555']
# web_pages must be one of type homepage, profile, work, or blog
contact.web_pages['homepage'] = ['https://Google.com']
# im_addresses must be one of type gtalk, aim,
# yahoo, lync, skype, qq, msn, icc, or jabber
contact.im_addresses['gtalk'] = 'Google'

# Save the contact to Nylas and the 3rd party provider
contact.save()

contact = nylas.contacts.get(new_contact_id)
pp_contact = pprint.PrettyPrinter(indent=4)
pp_contact.pprint(contact)
