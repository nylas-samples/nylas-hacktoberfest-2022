import Nylas from 'nylas';
import dotenv from 'dotenv';

dotenv.config();

Nylas.config({clientId: process.env.CLIENT_ID, clientSecret: process.env.CLIENT_SECRET});


// Get an account specified by a specific id
Nylas.accounts.find(process.env.ACCOUNT_ID)
  .then(account => console.log(`
    Account ID: ${account.id}
    Email: ${account.emailAddress}
    Provider: ${account.provider}
  `))
  .catch(e => console.error(e.message))
