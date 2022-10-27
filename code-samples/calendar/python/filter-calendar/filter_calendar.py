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


calendar_id = os.environ.get("CALENDAR_ID")

character_to_search = 'maha'

# Filter events based on the criteria : Last 10 entries of events that contain the word coffee! 
events = nylas.events.where(calendar_id=calendar_id,title=character_to_search,limit=10)


# Print formatted event details 
for event in events: 
    print("ID: {} | Title: {} | Date: {} | Participants: {}\n".format(
        event.id,
        event.title, 
        event.when["date"],
        event.participants
        ))