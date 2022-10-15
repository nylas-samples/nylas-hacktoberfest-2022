import  Nylas from "nylas";
import 'dotenv/config';
import Contact from "nylas/lib/models/contact";

Nylas.config({
    clientId: process.env.CLIENT_ID as string,
    clientSecret: process.env.CLIENT_SECRET as string,
});

const nylas = Nylas.with(process.env.ACCESS_TOKEN as string);

// Reading the last 3 emails
nylas.messages.list({limit: 3}).then(messages =>{
  for (let message of messages) {
    const sender = message.from[0];

    // Creating the contacts
    const contact = new Contact(nylas, {
      givenName: sender.name,
      notes: message.subject,
      emailAddresses: [{type: 'work', email: sender.email}]
    });

    // Saving the contact
    contact
      .save()
      .then(c => {
        console.log("Contact created:");
        console.log(`ID: ${c.id}`);
        console.log(`Name: ${c.givenName}`);
        console.log(`Notes: ${c.notes}`);
      });
  }
});


