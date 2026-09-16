# CodeAlpha Task 3 - Secure Coding Review

## Objective

The objective of this project is to review a Python Flask
application and identify security vulnerabilities.

## Technology Used

- Python
- Flask
- SQLite
- Bandit

## Vulnerabilities Identified

### 1. SQL Injection
User input was directly concatenated into an SQL query.

### 2. Insecure Password Handling
The original code directly used the password in the SQL query.

### 3. Credentials in URL
The original application accepted credentials through GET parameters.

## Recommendations

- Use parameterized SQL queries.
- Use secure password hashing and verification.
- Use POST requests for login credentials.
- Use HTTPS.
- Validate user input.
- Follow secure coding practices.

## Remediation

The SQL query was changed to use parameterized input and the
login endpoint was changed to use POST.

## Security Tool

Bandit was used for static analysis of the Python code.

## Conclusion

The code review identified security weaknesses and demonstrated
how secure coding practices can reduce application security risks.
