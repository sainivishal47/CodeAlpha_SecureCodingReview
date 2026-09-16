# Secure Coding Review

A security-focused Python Flask application demonstrating vulnerability identification, static code analysis, and secure coding practices.

## Project Overview

This project is created for **CodeAlpha Cyber Security Internship - Task 3: Secure Coding Review**.

The project demonstrates how a Python Flask application can be reviewed for security vulnerabilities using:

- Manual source-code inspection
- Bandit static security analysis
- Secure coding recommendations
- Vulnerability remediation techniques

The intentionally vulnerable application is included for educational security testing.

## Quick Start

Follow these steps to run the project locally.

### Step 1 - Clone the Repository

Open Terminal / Command Prompt and run:

```bash
git clone https://github.com/sainivishal47/CodeAlpha_SecureCodingReview.git
cd CodeAlpha_SecureCodingReview
```

### Step 2 - Run the Application

#### Linux / Kali / macOS

```bash
python3 app.py
```

#### Windows

```cmd
python app.py
```

### Step 3 - Open in Browser

After starting the application, open:

```text
http://127.0.0.1:5000/
```

You should see the **CodeAlpha Secure Coding Review** application.

### Stop the Application

To stop the Flask server, press:

```text
CTRL + C
```

## Project Files

- `app.py` - Simplified Flask application used for the secure coding demonstration.
- `vulnerable_app.py` - Intentionally vulnerable Flask application used for security analysis.
- `requirements.txt` - Python dependencies required to run and analyze the project.
- `README.md` - Project documentation.
- `.gitignore` - Prevents unnecessary and sensitive files from being committed.

## Project Structure

```text
CodeAlpha_SecureCodingReview/
├── app.py
├── vulnerable_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

Before running the project, make sure you have:

- Python 3
- pip
- Git
- A web browser

The project uses the following Python packages:

- **Flask** - Web application framework used to run the Flask application.
- **Bandit** - Static security analysis tool used to identify security issues in Python code.

## Security Analysis with Bandit

Bandit is a static security analysis tool for Python applications.

It helps identify common security problems in Python source code.

### Scan the Vulnerable Application

Run:

```bash
bandit vulnerable_app.py
```

The intentionally vulnerable application contains a potential **SQL Injection** issue caused by constructing an SQL query using user-controlled input.

Bandit identifies:

```text
B608 - Possible SQL injection vector through string-based query construction
```

### Vulnerability Details

- **Vulnerability:** SQL Injection
- **CWE:** CWE-89
- **Bandit Rule:** B608
- **Severity:** Medium
- **Confidence:** Low

## Vulnerable Code

The vulnerable application contains the following SQL query construction:

```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
```

The application directly combines user-controlled input with an SQL statement.

This can allow specially crafted input to modify the intended SQL query.

Therefore, this code represents a potential SQL Injection vulnerability.

## Secure Coding Recommendations

The following secure coding practices are recommended:

1. Use parameterized SQL queries instead of string concatenation.
2. Validate and sanitize user input.
3. Never store passwords in plain text.
4. Use secure password hashing for authentication systems.
5. Never hardcode passwords, API keys, or access tokens.
6. Use HTTPS when handling sensitive information.
7. Avoid exposing sensitive information through error messages.
8. Use static security analysis tools such as Bandit.
9. Keep vulnerable demonstration code isolated from production code.
10. Regularly review application dependencies for security updates.

## SQL Injection Remediation

A safer database implementation should use parameterized SQL queries.

Example:

```python
query = """
SELECT username, password_hash
FROM users
WHERE username = ?
"""

result = conn.execute(query, (username,)).fetchone()
```

Parameterized queries separate SQL instructions from user-provided data and help prevent user input from being interpreted as SQL syntax.

The current `app.py` is a simplified educational demonstration and does not contain the vulnerable database query.

## Scan the Current Application

Run:

```bash
bandit app.py
```

The current application was scanned with Bandit and reported:

```text
Total issues: 0
```

This demonstrates the use of static security analysis as part of the secure coding review process.

## Testing

The application was tested locally using:

```bash
python3 app.py
```

The web application was accessed through:

```text
http://127.0.0.1:5000/
```

Security testing was performed using:

```bash
bandit vulnerable_app.py
```

and:

```bash
bandit app.py
```

## Technologies Used

- Python 3
- Flask
- SQLite
- Bandit
- Kali Linux
- Git
- GitHub

## Learning Objectives

This project demonstrates:

- Secure source-code review
- SQL Injection identification
- Static security analysis
- Secure coding practices
- Vulnerability remediation
- Python Flask application development
- Git and GitHub workflow
- Basic cybersecurity testing

## Disclaimer

`vulnerable_app.py` intentionally contains insecure code for educational and security-review purposes.

It should **not** be deployed in a production environment.

Use this project only for authorized local testing and cybersecurity education.

## Conclusion

This project demonstrates a basic secure coding review process for a Python Flask application.

The review identified a potential SQL Injection vulnerability in the intentionally vulnerable application. Bandit was used to perform static security analysis and identify the risky SQL construction pattern.

The project also demonstrates secure coding recommendations, SQL Injection remediation using parameterized queries, and security testing practices.

