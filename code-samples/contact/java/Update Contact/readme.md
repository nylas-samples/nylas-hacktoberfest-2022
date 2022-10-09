# java-contact-update

This sample will show you to easily update a contact with the Nylas Java SDK.

## Setup

### System dependencies

- Java 1.8

### Install dependencies

```xml
<dependency>
   <groupId>com.nylas.sdk</groupId>
   <artifactId>nylas-java-sdk</artifactId>
    <version>1.18.0</version>
</dependency>
```

## Usage

Run the UpdateContact `.java` on your IDE or to run on cmd execute two commands along with file in the current working directory:

```bash
C:\com\nylas> javac UpdateContact.java
C:\com\nylas> java UpdateContact
```

When the contact is successfully updated, you'll get the updated contact object printed in the terminal :

```text
12:31:43.403 [main] DEBUG com.nylas.http.Body - <= No response body
Contact [ ... ]
```

## Learn more

Visit our [Nylas Node.js SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.
