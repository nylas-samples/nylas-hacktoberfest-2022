package com.example;

import com.nylas.Thread;
import com.nylas.*;

import java.io.IOException;
import java.util.List;

public class EmailFilter {

    public static void main(String[] args) throws RequestFailedException, IOException {
        String searchKeyword = "unsubscribe";
        NylasClient nylas = new NylasClient();
        NylasAccount account = nylas.account("l139C1ZR1BkX5OvlHBExLZWGE6iywx");
        List<Thread> threads = account.threads().list(new ThreadQuery().subject(searchKeyword).limit(10)).fetchAll();
        threads.forEach(thread -> {
            System.out.printf(
                    "Subject: %s | MessageId: %s %n",
                    thread.getSubject(),
                    thread.getMessageIds()
            );
        });
    }
}
