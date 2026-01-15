import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "output.json"


def fetch_api_data(url):
    """Fetch data from a public API."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error fetching API data: {error}")
        return []


def process_user_data(users):
    """Extract meaningful information from API response."""
    processed_data = []

    for user in users:
        user_info = {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"],
        }

        processed_data.append(user_info)

    return processed_data


def save_to_json_file(data, filename):
    """Save processed data into a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\nProcessed data saved successfully to {filename}")


def display_data(data):
    """Print processed data to terminal."""
    print("Fetched User Details:\n")

    for user in data:
        print(f"ID       : {user['id']}")
        print(f"Name     : {user['name']}")
        print(f"Username : {user['username']}")
        print(f"Email    : {user['email']}")
        print(f"City     : {user['city']}")
        print(f"Company  : {user['company']}")
        print("-" * 40)


def main():
    users = fetch_api_data(API_URL)

    if users:
        processed_data = process_user_data(users)
        display_data(processed_data)
        save_to_json_file(processed_data, OUTPUT_FILE)
    else:
        print("No data received from API.")


if __name__ == "__main__":
    main()
