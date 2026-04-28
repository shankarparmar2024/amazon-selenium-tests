# Amazon Automation Testing Project (Selenium + LambdaTest)

## Project Overview

This project demonstrates automated end-to-end testing of Amazon’s product search and cart functionality using Selenium WebDriver. The implementation includes product search, cart operations, price extraction, parallel execution, and cloud-based test execution on LambdaTest.

---

## Test Scenarios

### Test Case 1: iPhone Search and Add to Cart

* Navigate to Amazon
* Search for "iPhone"
* Select a product from results
* Add the product to the cart
* Extract and print the product price in the console

### Test Case 2: Galaxy Search and Add to Cart

* Navigate to Amazon
* Search for "Galaxy device"
* Select a product from results
* Add the product to the cart
* Extract and print the product price in the console

### Parallel Execution

* Both test cases are configured to run in parallel
* Improves execution efficiency and reflects real-world automation practices

---

## Tech Stack

* Programming Language: JavaScript / Java / Python (based on implementation)
* Automation Tool: Selenium WebDriver
* Test Runner: Playwright / TestNG / Mocha
* Cloud Platform: LambdaTest
* Version Control: Git and GitHub

---

## LambdaTest Execution (Bonus Task)

The test suite has been executed successfully on LambdaTest Cloud.

* Test ID: DA-WIN-3114244-1777378714321379642MVJ
* Platform: Windows 11
* Browser: Chrome
* Resolution: 1920x1080
* Execution Mode: Parallel

---

## Screenshots

Add your LambdaTest screenshots in the `screenshots/` directory and reference them below:

* LambdaTest Dashboard
* iPhone Test Execution
* Galaxy Test Execution

Example:

```
![Dashboard](./screenshots/dashboard.png)
```

---

## Project Structure

```
amazon-selenium-tests/
│
├── tests/
│   ├── iphoneTest.js
│   ├── galaxyTest.js
│
├── utils/
│   └── driverSetup.js
│
├── config/
│   └── config.js
│
├── screenshots/
│
├── package.json / pom.xml
├── README.md
└── .gitignore
```

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/shankarparmar2024/amazon-selenium-tests.git
cd amazon-selenium-tests
```

### Install Dependencies

```bash
npm install
```

(or use Maven/requirements.txt depending on your setup)

---

### Run Tests Locally

```bash
npx playwright test
```

or

```bash
npm test
```

---

### Run Tests on LambdaTest

1. Create an account at https://www.lambdatest.com/
2. Add credentials in your configuration file or environment variables:

```bash
LT_USERNAME=your_username
LT_ACCESS_KEY=your_access_key
```

3. Execute tests:

```bash
npx playwright test --config=lt.config.js
```

---

## Key Features

* End-to-end automation of real-world scenarios
* Dynamic element handling on a production website
* Product price extraction and logging
* Parallel test execution
* Cloud execution using LambdaTest
* Maintainable and scalable project structure

---

## Learning Outcomes

* Practical experience with Selenium WebDriver
* Handling dynamic UI elements and locators
* Implementing parallel execution strategies
* Running tests on cloud infrastructure
* Structuring automation projects for scalability

---

## Submission Details

* Repository: https://github.com/shankarparmar2024/amazon-selenium-tests
* Parallel Execution: Implemented
* LambdaTest Execution: Completed
* README Documentation: Included

---

## Author

Sumit Parmar
GitHub: https://github.com/shankarparmar2024
