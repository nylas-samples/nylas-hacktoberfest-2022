# java-contact-create

This sample will show you to easily create a contact with the Nylas Java SDK.

## Project Folder Structure

```text
code-samples
├── ...
├── contact                   
│   ├── java          
│       ├── Create Contact
│                        ├── src/main/java
│                                        ├── CreateContact.java
│                                        ├── readme.md
│                        ├── pom.xml                                                        
│   └── ...              
└── ...
```

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

Run the CreateContact `.java` on your IDE or to run on terminal, execute below maven command along with pom `.xml` and CreateContact in the current working directory:

```bash
mvn exec:java -Dexec.mainClass=CreateContact
```

When the contact is successfully created, you'll get the newly created contact object printed in the terminal :

```text
Contact [ ... ]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  20.867 s
[INFO] Finished at: 2022-10-12T14:12:26+05:30
[INFO] ------------------------------------------------------------------------
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.
