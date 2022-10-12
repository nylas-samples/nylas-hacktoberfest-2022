import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.nylas.Contact;
import com.nylas.NylasAccount;
import com.nylas.NylasClient;
import com.nylas.RequestFailedException;

public class CreateContact {
	
	public static void main(String[] args) throws IOException, RequestFailedException {

	    // Create client object and connect it to Nylas using
	    // an account's access token
	    NylasClient client = new NylasClient();

	    // Provide the access token for a specific account
	    NylasAccount account = client.account("ACCESS_TOKEN");
	    
	    // Initialize a new contact object
	    Contact contact = new Contact();

	    // Assign values to the object
	    contact.setGivenName("Ashley");
	    contact.setSurname("Brad");
	    contact.setBirthday("11-01-1991");
	    contact.setCompanyName("Microsoft");
	    contact.setJobTitle("Senior Software Engineer");
	    contact.setManagerName("Jen");

	    List<Contact.Email> emails = new ArrayList<>();
	    emails.add(new Contact.Email("Gmail", "ashleybrad@gmail.com"));
	    contact.setEmails(emails);
	    
	    List<Contact.PhoneNumber> phoneNumbers = new ArrayList<>();
	    phoneNumbers.add(new Contact.PhoneNumber("Work", "1010101010"));
	    contact.setPhoneNumbers(phoneNumbers);

	    //Create the contact object
	    contact = account.contacts().create(contact);

	    //Print the updated object
	    System.out.println(contact.toString());

	  } 
}
