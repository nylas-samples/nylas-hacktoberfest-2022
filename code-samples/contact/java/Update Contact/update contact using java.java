package com.nylas;

import java.util.List;
import java.io.IOException;

public class UpdateContact {

	public static void main(String[] args) throws IOException, RequestFailedException {

	    // Create client object and connect it to Nylas using
	    // an account's access token
	    NylasClient client = new NylasClient();
	    
	    // Provide the access token for a specific account
	    NylasAccount account = client.account("sDaBh6NmnBKxBhZOF10yEs8b6QL05D");
	    
	    //Retrieve the contact object to update with contact id
	    Contact contact = account.contacts().get("82u83w6fu9c8kvzm70c34ko04");

	    //Update the contact object attributes
	    contact.setCompanyName("Microsoft");
	    contact.setJobTitle("Senior Software Engineer");
	    contact.setManagerName("Jen");
	    
	    List<Contact.Email> emails = contact.getEmails();
	    emails.add(new Contact.Email("Outlook", "ashleybrad@outlook.com"));
	    contact.setEmails(emails);
	    
	    //Update the contact object
	    contact = account.contacts().update(contact);
	    
	    //Print the updated object
	    System.out.println(contact.toString());
	    
	  } 
}
