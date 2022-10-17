const Nylas = require('nylas')
const { default: Draft } = require('nylas/lib/models/draft')

require('dotenv').config()

Nylas.config({
   clientId: process.env.CLIENT_ID,
   clientSecret: process.env.CLIENT_SECRET
})

const nylas = Nylas.with(process.env.ACCESS_TOKEN)
const draft = new Draft(nylas, {
  subject: 'Creating a draft',
  body: 'This is where a draft is created',
  to: [{ name: 'You', email: 'you@nylas.com' }]
})

draft.save()