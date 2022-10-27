import os
from dotenv import load_dotenv
from nylas import APIClient
import datetime

# Loading all the environment variables from `.env` file
load_dotenv()

nylas = APIClient(
   os.environ.get("CLIENT_ID"),
   os.environ.get("CLIENT_SECRET"),
   os.environ.get("ACCESS_TOKEN"),
)

# # Create a calendar
# calendars = nylas.calendars.all()

# for calendar in calendars:
#   print("Id: {} | Name: {} | Description: {}".format(
#           calendar.id, calendar.name, calendar.description))


calendar_id = os.environ.get("CALENDAR_ID")

character_to_search = 'coffee'

# Filter events based on the criteria : Last 10 entries of events that contain the word coffee! 
events = nylas.events.where(calendar_id=calendar_id,title=character_to_search,limit=10)

# Sometimes for few calendars, wither [date] exists or [start_time]. This keyword is to accommodate both the scenarios. 
# This also handles the case where in case of [start_time], the epoch is being converted to a readable datetime format. 
def get_proper_date():
    if "date" in event.when: 
        # print("Key [date] Exists")
        return event.when["date"]
    elif "start_time" in event.when:
        # print("Key [start_time] Exists") 
        st_time = event.when["start_time"]
        datetime_var = datetime.datetime.fromtimestamp(st_time)
        return str(datetime_var).split(' ')[0]

# Print formatted event details 
for event in events: 
    print("ID: {} | Title: {} | Date: {} | Participants: {}\n".format(
        event.id,
        event.title, 
        get_proper_date(),
        event.participants
        ))