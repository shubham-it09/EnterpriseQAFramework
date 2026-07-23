# Enterprise QA Framework

## Overview

Enterprise QA Framework is a scalable and modular automation framework built using **Playwright**, **Pytest**, and **HTTPX**. It supports both **UI Automation** and **API Automation** with a clean layered architecture following enterprise software engineering principles.

The framework is designed to be:

- Scalable
- Maintainable
- Reusable
- CI/CD Ready
- Parallel Execution Ready
- AI Ready (Future Enhancements)

---

# Features

## UI Automation

- Playwright (Python)
- Page Object Model (POM)
- Business Layer
- BasePage Implementation
- Browser Fixtures
- Context Fixtures
- Page Fixtures
- Screenshot on Failure
- Logging
- Allure Reporting
- Parallel Execution using pytest-xdist
- Timestamped Artifacts
- Configuration Management

---

## API Automation

- HTTPX Client
- Generic API Client
- Business Layer
- Endpoint Layer
- Authentication Support
- CRUD Operations

    - GET
    - POST
    - PUT
    - PATCH
    - DELETE

- Request Models (Dataclasses)
- JSON Test Data
- File Utilities

---

## Reporting

- Allure Reports
- Failure Screenshots
- Execution Logs
- Timestamped Execution Artifacts

---

## Framework Capabilities

- Modular Architecture
- Reusable Components
- Generic Test Runner
- Batch Script Execution
- Local Pipeline
- CI/CD Ready

---

# Tech Stack

| Technology | Version |
|------------|---------|
| Python | 3.13 |
| Playwright | Latest |
| Pytest | Latest |
| HTTPX | Latest |
| Allure | 2.44.0 |
| Java | 17 |
| Pytest-xdist | Latest |

---

# Project Structure

EnterpriseQAFramework

```
EnterpriseQAFramework
│
├── api
│   ├── business
│   ├── client
│   ├── endpoints
│   ├── fixtures
│   ├── models
│   └── tests
│
├── business
│
├── config
│
├── core
│
├── fixtures
│
├── pages
│
├── testdata
│
├── tests
│
├── artifacts
│
├── scripts
│   ├── setup_environment.bat
│   ├── clean_reports.bat
│   ├── run_tests.bat
│   ├── serve_allure.bat
│   └── run_framework.bat
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Framework Architecture

## UI Framework

```
Tests
    │
    ▼
Business Layer
    │
    ▼
Page Objects
    │
    ▼
BasePage
    │
    ▼
Playwright
```

---

## API Framework

```
Tests
    │
    ▼
Business Layer
    │
    ▼
Endpoints
    │
    ▼
API Client
    │
    ▼
HTTPX
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

## Run UI Tests

```bash
pytest tests
```

or

```bash
scripts\run_framework.bat ui
```

---

## Run API Tests

```bash
pytest api/tests
```

or

```bash
scripts\run_framework.bat api
```

---

## Run Complete Framework

```bash
scripts\run_framework.bat all
```

---

# Allure Report

Run Report

```bash
allure serve artifacts\allure-results
```

---

# Batch Scripts

| Script | Description |
|---------|-------------|
| run_framework.bat | Executes complete framework |
| run_tests.bat | Generic Pytest runner |
| clean_reports.bat | Cleans previous execution artifacts |
| serve_allure.bat | Opens Allure Report |
| setup_environment.bat | Initial environment setup |

---

# Current Implemented Features

## UI

- Login Automation
- Admin Module
- Screenshot on Failure
- Logging
- Parallel Execution
- Allure Reporting

---

## API

- Authentication
- Create Booking
- Get Booking
- Update Booking
- Partial Update Booking
- Delete Booking

---

# Future Roadmap

## CI/CD

- Jenkins Integration
- GitHub Actions
- Azure DevOps
- Docker

---

## API Framework

- Negative Testing
- Schema Validation
- API Assertion Library
- Response Models
- Advanced Logging

---

## UI Framework

- Data Driven Framework
- Excel Support
- Database Validation

---

## AI Features

- AI Test Case Generation
- AI API Test Generation
- AI Failure Analysis
- AI Locator Healing
- AI Bug Summarization
- AI Report Analyzer

---

# Design Principles

The framework follows the following software engineering principles:

- Single Responsibility Principle (SRP)
- Don't Repeat Yourself (DRY)
- Layered Architecture
- Separation of Concerns
- Reusability
- Maintainability
- Scalability

---

# Author

**Shubham Pandey**



Automation | Playwright | API Automation | Python | Java | CI/CD | AI in Testing