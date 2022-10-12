import os
from dotenv import load_dotenv
from nylas import APIClient

# Loading all the environment variables from `.env` file
load_dotenv()

nylas = APIClient(
   os.environ.get("CLIENT_ID"),
   os.environ.get("CLIENT_SECRET")
)

# Get an account specified by a specific id
account = None

try:
  account = nylas.accounts.get(os.environ.get("ACCOUNT_ID"))
except Exception as e:
  print(e)
else:
  print(
    f"""
      Account ID: {account.id}
      Email: {account.email}
      Provider: {account.provider}
    """
  )