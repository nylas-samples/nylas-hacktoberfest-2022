# Filter Calendar Event using Nylas Python SDK

  

## Setup

  

1) In the root folder, create a .env file with your nylas configuration as follow

  

```bash

CLIENT_ID="YOUR_CLIENT_ID"

CLIENT_SECRET="YOUR_CLIENT_SECRET"

ACCESS_TOKEN="YOUR_NYLAS_ACCESS_TOKEN"

```

  

1) Install dependencies

  

```bash

python -m pip install nylas dotenv

```

  

## Usage

  

Update the `.env` file with the desired Calendar ID to fetch events from: 

  

```bash

CALENDAR_ID = "YOUR_CALENDAR_ID"

```

  

## Output

  

When the calendar is successfully filtered with keyword `maha`, the filtered events will be displayed:

  

```text

ID: a0b95z1x8ldj2yn6rmsorf5cj | Title: Mahatma Gandhi Jayanti | Date: 2022-10-02 | Participants: []

ID: dqym8385kos4ipkn9xroyzctj | Title: Maha Saptami | Date: 2022-10-02 | Participants: []

ID: 59y8awgqdslji20q2kn2trhzy | Title: Maha Ashtami | Date: 2022-10-03 | Participants: []

ID: 92q7aljxtbmlo19ydffox7ukm | Title: Maha Navami | Date: 2022-10-04 | Participants: []

ID: 4qpw7iwmrctucagj9gb5ggz4e | Title: Maharishi Valmiki Jayanti | Date: 2022-10-09 | Participants: []

ID: cnfpcemda9o989j66bw0rrpil | Title: Maharishi Dayanand Saraswati Jayanti | Date: 2023-02-15 | Participants: []

ID: 31jl1px2lmchk39ry5h9qk9pi | Title: Maha Shivaratri/Shivaratri | Date: 2023-02-18 | Participants: []

ID: 47nz0wkzctit4zmwwlgg2o2br | Title: Mahavir Jayanti | Date: 2023-04-04 | Participants: []

ID: bmjbrihijof5fobk5hpezwkhy | Title: Mahatma Gandhi Jayanti | Date: 2023-10-02 | Participants: []

ID: a3ej95ueza6wv6cbi3v16rkh4 | Title: Maha Saptami | Date: 2023-10-21 | Participants: []

```