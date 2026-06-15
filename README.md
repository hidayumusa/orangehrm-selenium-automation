# Selenium Pytest POM Framework

Structure:

- `locators/login_locators.py` - locators for login page
- `pages/login_page.py` - page object with interactions
- `conftest.py` - pytest fixture to initialize/teardown the browser
- `test_login.py` - pytest tests for success and failure
- `requirements.txt` - Python dependencies

Run tests and generate an HTML report:

```bash
pip install -r requirements.txt
python -m pytest
```

The default report file is generated as `report.html` by `pytest.ini`.

Project Summary

This project is a Selenium Automation Testing Framework developed using Python, Pytest, and the Page Object Model (POM) design pattern for the OrangeHRM web application.

Key Features
Automated login validation using Selenium WebDriver.
Page Object Model (POM) structure for maintainable and reusable test scripts.
Automated navigation testing across OrangeHRM modules:
    Login
    PIM
    Admin
    Leave

Executes multiple test runs to simulate repeated test cycles.
Captures screenshots automatically when test failures occur.
Records execution results into a CSV report for reporting and analytics.
Tracks:
Test Case ID
Module
Scenario
Priority
Run Number
Test Status (Pass/Fail)
Error Type
Execution Time
Test Date
Tester Name
Screenshot Evidence
Generates structured test data suitable for Power BI dashboard visualization.

Test Execution Flow
Launch OrangeHRM application.
Execute login validation.
Navigate through selected modules.
Capture failures and screenshots automatically.
Log all test execution results.
Export results to CSV format for analysis and reporting.

Technologies Used
Python
Selenium WebDriver
Pytest
Page Object Model (POM)
CSV Reporting
Power BI Reporting Dashboard
Git & GitHub
