# java-calendar-filter

This sample will show you to easily filter last 10 email with a keyword using Nylas Java SDK.


## Setup

### System dependencies

- Java 11

### Install dependencies

```xml
<dependency>
   <groupId>com.nylas.sdk</groupId>
   <artifactId>nylas-java-sdk</artifactId>
   <version>1.18.0</version>
</dependency>
```

## Usage

Run the  `EmailFilter.java`  execute below maven command:

```bash
mvn exec:java -Dexec.mainClass=EmailFilter
```

When the calendar is successfully filtered with keyword `dinner`, the filtered events will be displayed:

```text
"Subject: Patricia, Thank you for ordering with us | MessageId: 34rkoomv2w6ie9wsiytny0fx
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.