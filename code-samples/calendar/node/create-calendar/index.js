import Nylas from 'nylas';
import dotenv from 'dotenv';

dotenv.config();

// Initiate config
Nylas.config({
    clientId: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
    accessToken: process.env.ACCESS_TOKEN
});

// Create the calendar
Nylas.calendars.create({
    name: "Nylas Calendar",
    description: "Nylas Calendar for #Hacktoberfest2022",
    location: "Github",
    timezone: "Asia/Jakarta"
}).then((calendar) => {
    // Succesfull result
    console.log(
        `Name: ${calendar.name}`,
        `Description: ${calendar.description}`,
        `Location: ${calendar.location}`,
        `Timezone: ${calendar.timezone}`,
    )
}).catch((error) => {
    // Error result
    console.log(error.message)
});