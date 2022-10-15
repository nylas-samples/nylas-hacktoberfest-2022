const dotenv = require("dotenv");
const Nylas = require("nylas");
const { default: Calendar } = require("nylas/lib/models/calendar");

dotenv.config();

// Initiate config
Nylas.config({
    clientId: process.env.CLIENT_ID ,
    clientSecret: process.env.CLIENT_SECRET 
});

const nylas = Nylas.with(process.env.ACCESS_TOKEN );

const calendar = new Calendar(nylas, {
  name: 'Nylas #Hacktoberfest2022',
  description: 'Nylas #Hacktoberfest2022',
  location: 'Github',
  timezone: 'Asia/Jakarta'
});

calendar.save()
    .then((c) => {
        console.log(`Calendar created successfully`)
        console.log(`Name : ${c.name}`);
        console.log(`Description : ${c.description}`);
        console.log(`Location : ${c.location}`);
        console.log(`Timezone : ${c.timezone}`);
    })
    .catch((err) => console.log(err));