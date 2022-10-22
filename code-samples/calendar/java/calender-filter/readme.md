# java-calendar-filter

This sample will show you to easily filter last 10 calendar event with a keyword using Nylas Java SDK.


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

Run the  `CalenderFilter.java`  execute below maven command:

```bash
mvn exec:java -Dexec.mainClass=CalenderFilter
```

When the calendar is successfully filtered with keyword `dinner`, the filtered events will be displayed:

```text
Title: Mom’s birthday, dinner at Kazoku | Description: null | CalenderId: 7mchh8gnlvihlstcwkinultj3 
Title: dinner with Michal and Neela 7pm at Gamma Gamma | Description: null | CalenderId: 7mchh8gnlvihlstcwkinultj3 
```

## Learn more

Visit our [Nylas Java SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/java-sdk/) to learn more.