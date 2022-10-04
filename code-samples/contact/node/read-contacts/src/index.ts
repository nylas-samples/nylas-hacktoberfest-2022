import  Nylas from "nylas";
import 'dotenv/config';
import Contact from "nylas/lib/models/contact";

Nylas.config({
    clientId: process.env.CLIENT_ID as string,
    clientSecret: process.env.CLIENT_SECRET as string,
});

const nylas = Nylas.with(process.env.ACCESS_TOKEN as string);

nylas.contacts.list({limit: 10}).then((contacts: Contact[]) => {
  for (const contact of contacts) {
     const { id, givenName, surname, emailAddresses } = contact;
     
      console.log(`Name: ${givenName} ${surname} | Emails: ${emailAddresses?.join(',')} | ID: ${id}`);
  }
});
