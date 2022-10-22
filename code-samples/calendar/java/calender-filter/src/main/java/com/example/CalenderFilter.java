package com.example;

import com.nylas.*;

import java.io.IOException;
import java.util.List;


/**
 * List last 10 calendar events that contain a keyword, like 'coffee'
 */

public class CalenderFilter {

    public static void main(String[] args) throws RequestFailedException, IOException {
        String searchKeyword = "coffee";
        NylasClient nylas = new NylasClient();
        NylasAccount account = nylas.account(System.getenv("ACCESS_TOKEN"));
        List<Event> events = account.events().list(new EventQuery().title(searchKeyword).limit(10)).fetchAll();
        events.forEach(event -> {
            System.out.printf(
                    "Title: %s | Description: %s | CalenderId: %s",
                    event.getTitle(),
                    event.getDescription(),
                    event.getCalendarId()
            );
        });
    }
}
