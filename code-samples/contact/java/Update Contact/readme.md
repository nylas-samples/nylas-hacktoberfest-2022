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

Run the UpdateContact `.java` on your IDE or to run on terminal, execute below maven command along with pom `.xml` and UpdateContact in the current working directory:

```bash
mvn exec:java  -Dexec.mainClass=UpdateContact
```

When the contact is successfully updated, you'll get the updated contact object printed in the terminal :

```text
Contact [ ... ]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  20.818 s
[INFO] Finished at: 2022-10-11T16:52:53+05:30
[INFO] ------------------------------------------------------------------------
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.
