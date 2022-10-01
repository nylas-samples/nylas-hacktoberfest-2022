import  Nylas from "nylas";

Nylas.config({
    clientId: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
});

const nylas = Nylas.with(process.env.ACCESS_TOKEN);

nylas.contacts.list({limit: 10}).then(contacts => {
  for (const contact of contacts) {
      console.log(`Name: ${contact.givenName} ${contact.surname} | Email: ${contact.emailAddresses[0]['email']} | ID: ${contact.id}`);
  }
});
