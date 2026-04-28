# Amazon Automation Testing Project (Selenium + LambdaTest)

## Project Overview

This project demonstrates automated end-to-end testing of Amazon’s product search and cart functionality using Selenium WebDriver. The implementation includes product search, cart operations, price extraction, parallel execution, and cloud-based test execution on LambdaTest.

---

## Test Scenarios
<img width="960" height="504" alt="Screenshot 2026-04-28 182106" src="https://github.com/user-attachments/assets/e846188c-2ee3-48da-9db4-0e24bce2550e" />


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

* Programming Language: JavaScript ,Java , Python (based on implementation)
* Automation Tool: Selenium WebDriver
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

<img width="960" height="504" alt="Screenshot 2026-04-28 175713" src="https://github.com/user-attachments/assets/f972460e-9af5-4fd6-a1e7-8315b141ebde" />


* LambdaTest Dashboard
* iPhone Test Execution
* Galaxy Test Execution

<img width="960" height="504" alt="Screenshot 2026-04-28 175851" src="https://github.com/user-attachments/assets/1e7ca3ef-3d9b-448e-bf6c-12c32d15c126" />

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

Shankar suman singh parmar 
GitHub: https://github.com/shankarparmar2024
