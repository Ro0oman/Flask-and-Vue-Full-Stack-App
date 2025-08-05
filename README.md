# my-app

A simple "Hello World" Java application built with Apache Maven. This project serves as a basic template for a Maven-based Java project.

## Description

This is a minimal Java application that prints "Hello World!" to the console. It is configured with a `pom.xml` for dependency management and building with Maven. It also includes a simple JUnit test case to demonstrate testing capabilities.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Java Development Kit (JDK)** - Version 1.7 or later (as configured in `pom.xml`).
*   **Apache Maven** - To build and manage the project.

You can verify your installations by running `java -version` and `mvn -version` in your terminal.

## Getting Started

### Building the Project

To compile the source code, run the tests, and package the application into a JAR file, execute the following command from the project's root directory:

```bash
mvn clean package
```

This command will create a `target` directory containing the compiled classes and the executable JAR file (`my-app-1.0-SNAPSHOT.jar`).

### Running the Application

Once the project is built, you can run the application using the following command:

```bash
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

You should see the following output in your console:
```
Hello World!
```

### Running Tests

To run the unit tests for the project, use the following Maven command:

```bash
mvn test
```

This will execute the tests defined in `src/test/java` and provide a report on their execution.

## Project Structure

```
.
├── pom.xml                # Maven Project Object Model
└── src
    ├── main
    │   └── java
    │       └── com/mycompany/app/App.java   # Main application class
    └── test
        └── java
            └── com/mycompany/app/AppTest.java # Unit test for App
```