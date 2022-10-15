import os
from dotenv import load_dotenv
from nylas import APIClient

# Loading all the environment variables from `.env` file
load_dotenv()

nylas = APIClient(
   os.environ.get("CLIENT_ID"),
   os.environ.get("CLIENT_SECRET"),
   os.environ.get("ACCESS_TOKEN"),
)

# Create a calendar
calendar = nylas.calendars.create()
calendar.name = "Nylas Calendar"
calendar.description = "My Nylas Calendar for Hacktoberfest"
calendar.location = "Location Description"
calendar.timezone = "America/Los_Angeles"

calendar.save()


print(f'''
  ID: {calendar.id}
  Account: {calendar.account_id}
  Name: {calendar.name}
  Description: {calendar.description}
  Location: {calendar.location}
''')
