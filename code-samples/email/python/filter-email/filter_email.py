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

# Keyword to search under subject 
subject_to_search = 'unsubscribe'

# Perform a search operation on the subject based on the keyword, and limit it to last 10 emails.
for thread in nylas.messages.search("subject:"+subject_to_search, limit=10):
    print(thread.subject)  

