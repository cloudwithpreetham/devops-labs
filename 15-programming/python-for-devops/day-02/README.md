# Day 02 – Automating System Tasks with Python

## Overview

Today’s task focused on using Python to interact with a public API, parse JSON data, extract useful information, display it in the terminal, and save the processed output into a JSON file.

This is an important DevOps skill because modern infrastructure tools such as cloud platforms, Kubernetes, CI/CD systems, and monitoring tools are heavily API-driven.

---

## Task Objective

Create a Python script that:

- Calls a public API
- Fetches data using the `requests` library
- Parses the JSON response
- Extracts meaningful information
- Prints the processed output to the terminal
- Saves the processed data into a JSON file

---

## Tools and Technologies Used

- Python 3
- requests library
- JSON
- VS Code
- Linux terminal
- Git and GitHub

---

## Project Structure

```bash
day-02/
├── api_data_fetcher.py
├── output.json
├── README.md
├── reference.md
└── screenshots/
```

---

## API Used

For this task, I used the JSONPlaceholder public API:

```bash
https://jsonplaceholder.typicode.com/users
```

This API returns sample user data in JSON format.

---

## Python Script

File created:

```bash
api_data_fetcher.py
```

The script performs the following actions:

1. Sends a GET request to the public API.
2. Checks whether the API response is successful.
3. Converts the response into JSON using `.json()`.
4. Extracts selected fields from the response.
5. Prints the processed data in the terminal.
6. Saves the final result into `output.json`.

---

## Key Fields Extracted

From the API response, I extracted the following user information:

- ID
- Name
- Username
- Email
- City
- Company Name

Example processed structure:

```json
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "city": "Gwenborough",
  "company": "Romaguera-Crona"
}
```

---

## How to Run the Script

### Step 1: Move into the Day 02 directory

```bash
cd day-02
```

### Step 2: Install the required library

```bash
pip install requests
```

### Step 3: Run the Python script

```bash
python3 api_data_fetcher.py
```

---

## Output

After running the script, the processed API data is displayed in the terminal.

Example terminal output:

```bash
Fetched User Details:

ID       : 1
Name     : Leanne Graham
Username : Bret
Email    : Sincere@april.biz
City     : Gwenborough
Company  : Romaguera-Crona
----------------------------------------
ID       : 2
Name     : Ervin Howell
Username : Antonette
Email    : Shanna@melissa.tv
City     : Wisokyburgh
Company  : Deckow-Crist
----------------------------------------

Processed data saved successfully to output.json
```

---

## JSON Output File

The script generates a JSON output file:

```bash
output.json
```

This file stores the processed API response in a clean and readable JSON format.

To verify the file:

```bash
cat output.json
```

---

## Error Handling

Basic error handling was added using `try-except` and `raise_for_status()`.

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
except requests.exceptions.RequestException as error:
    print(f"Error fetching API data: {error}")
    return []
```

This helps handle issues such as:

- API not reachable
- Network timeout
- Invalid response
- HTTP errors

---

## What I Learned

Today I learned how to:

- Use Python to call a public API
- Fetch API data using the `requests` library
- Parse JSON data using `.json()`
- Work with dictionaries and lists
- Extract nested JSON values
- Save processed data into a JSON file
- Use functions to keep Python code clean and readable

---

## Why This Matters in DevOps

APIs are used everywhere in DevOps.

DevOps engineers commonly interact with APIs for:

- Cloud automation
- Kubernetes operations
- CI/CD pipelines
- Monitoring dashboards
- Alerting systems
- Infrastructure management
- Log and metric collection

Understanding API calls and JSON parsing is a strong foundation for automation.

---

## Files Created

| File                  | Purpose                                     |
| --------------------- | ------------------------------------------- |
| `api_data_fetcher.py` | Python script to fetch and process API data |
| `output.json`         | Stores processed API output                 |
| `README.md`           | Documentation of today’s task               |
| `reference.md`        | Notes and reference material                |
| `screenshots/`        | Proof of execution and output               |

---

## Final Status

Day 02 task completed successfully.

The Python script fetches API data, processes the JSON response, prints meaningful output in the terminal, and saves the result into a JSON file.
