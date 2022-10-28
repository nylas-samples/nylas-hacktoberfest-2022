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
to_email = os.environ.get("EMAIL_TO")

# Get today’s date
today = datetime.date.today()
# Today’s date at 12:00:00 am
START_TIME = int(datetime.datetime(today.year, today.month, today.day, 13, 10, 0).strftime('%s'))
# Today’s date at 11:59:59 pm
END_TIME = int(datetime.datetime(today.year, today.month, today.day, 14, 0, 0).strftime('%s'))
# Create event draft
event = nylas.events.create()

# Define event elements
event.title = "Coffee date to Discuss Hacktoberfest 2023!"
event.location = "MARS!"
event.when = {"start_time": START_TIME, "end_time": END_TIME}
event.recurrence = {'rrule': ['RRULE:FREQ=WEEKLY;WKST=SU;UNTIL=20221206T182959Z;BYDAY=MO'], 'timezone': 'Asia/Kolkata'}
event.participants = [{"name": "Elon Musk", "email": to_email}]
event.calendar_id = calendar_id
# We would like to notify participants
event.save(notify_participants=True)

if event.id:
  print("Event created successfully! See you Soon. ")
else:
  print("Oops! There was an error creating the event.")


# Verify if a recurring event is present in the Calendar. 
character_to_search = 'Coffee date to Discuss Hacktoberfest 2023!'

events = nylas.events.where(calendar_id=calendar_id,title=character_to_search)
# Get the recurrence and participant email from the first invite of the list and perform verification. 
# After that we will assume that for the remaining recurrences, same details are available.
for event in events: 
    if event.recurrence:
      print("Recurring event is generated successfully!")
    if event.participants[0]["email"] == to_email:
      print("Desired invitee's are present.")
    break