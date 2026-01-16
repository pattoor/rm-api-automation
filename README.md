# Rick and Morty API - Data Integrity & Automation Suite 🚀

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Pytest](https://img.shields.io/badge/framework-pytest-green.svg)
![Pydantic](https://img.shields.io/badge/validation-pydantic-red.svg)

This project is more than just a functional testing suite; it is a **Data Quality Engineering** framework. It is designed to ensure API contract integrity and data consistency through strict schema validation.

## 🎯 Project Objective
To ensure that any backend changes in the Rick and Morty API are immediately detected if they break the data structure expected by consumers (Frontend/Mobile), effectively reducing production bugs and integration issues.

## 👤 Who Is This For?
This project is intended for:
- Backend teams maintaining public or internal APIs
- Startups that need to ensure API stability without manual testing
- Data-driven teams that rely on consistent API contracts
- Projects where breaking API changes can silently impact frontend, mobile, or analytics systems

## 🏗️ Project Architecture
The project follows the **Service Layer** design pattern to decouple connection logic from test execution:

* **`models/`**: Data schema definitions using **Pydantic**. It acts as the "source of truth" for the data contract.
* **`services/`**: A custom HTTP client built on the **Requests** library, designed for reusability and scalability.
* **`tests/`**: Automated test suite powered by **Pytest**, utilizing parametrization to cover multiple scenarios with efficient, DRY code.
* **CI:** Optional GitHub Actions workflows can be added under `.github/workflows/` (not included in this repo).

## 🚀 Key Features
-   **Contract Testing:** Automatic validation of data types, URL formats, and mandatory fields.
-   **Negative Testing:** Handling and validation of error codes (404 Not Found, 400 Bad Request).
 -   **CI/CD Ready:** Designed for CI automation (GitHub Actions config not included).
-   **Professional Reporting:** Detailed execution logs and status reports.

## 💼 Business Impact
By automating API contract and data integrity validation, this approach helps teams:
- Detect breaking changes early in CI
- Reduce production bugs caused by unexpected API responses
- Prevent data inconsistencies from reaching analytics or ML pipelines
- Save engineering time otherwise spent on manual testing

## 🛠️ Installation & Execution

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/pattoor/rm-api-automation.git](https://github.com/pattoor/rm-api-automation.git)
    cd rm-api-automation
    ```

2.  **Configure Virtual Environment:**
    ```bash
    python -m venv env
    # Windows:
    .\env\Scripts\activate
    # Mac/Linux:
    source env/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Test Suite:**
    ```bash
    # Detailed mode
    python -m pytest -v

    # Short summary mode
    python -m pytest --tb=short
    ```

---
**Authored by Patricio Romero**  
Automation & API Reliability | Python  
Information Systems Engineering Student
