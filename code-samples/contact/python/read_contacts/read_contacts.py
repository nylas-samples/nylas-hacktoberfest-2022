from nylas import APIClient
import os

# Load your env variables
from dotenv import load_dotenv
load_dotenv()


# Add the client credentials to the environment variables
nylas = APIClient(
    os.environ.get("CLIENT_ID"),
    os.environ.get("CLIENT_SECRET"),
    os.environ.get("ACCESS_TOKEN"),
)

# Get All Contacts
contacts = nylas.contacts.all()
print(contacts)
