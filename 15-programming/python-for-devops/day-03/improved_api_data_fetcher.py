#!/usr/bin/env python3

"""
Day 03 - Improved API Data Fetcher

This script fetches public GitHub user data using the GitHub API.
It is improved with:
- Functions
- Basic exception handling
- Better variable names
- Cleaner output
- PEP8-style formatting
"""

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


def fetch_github_user(username):
    """
    Fetch GitHub user data from the GitHub API.
    """

    api_url = f"https://api.github.com/users/{username}"

    try:
        with urlopen(api_url, timeout=10) as response:
            response_data = response.read()
            return json.loads(response_data)

    except HTTPError as error:
        if error.code == 404:
            print(f"Error: GitHub user '{username}' was not found.")
        else:
            print(f"HTTP Error: {error.code} - Unable to fetch data.")
        return None

    except URLError:
        print("Error: Network issue. Please check your internet connection.")
        return None

    except json.JSONDecodeError:
        print("Error: Failed to parse API response.")
        return None

    except Exception as error:
        print(f"Unexpected error occurred: {error}")
        return None


def display_user_summary(user_data):
    """
    Display selected GitHub user details in a readable format.
    """

    print("\nGitHub User Summary")
    print("-------------------")
    print(f"Username     : {user_data.get('login', 'N/A')}")
    print(f"Name         : {user_data.get('name', 'N/A')}")
    print(f"Public Repos : {user_data.get('public_repos', 'N/A')}")
    print(f"Followers    : {user_data.get('followers', 'N/A')}")
    print(f"Following    : {user_data.get('following', 'N/A')}")
    print(f"Profile URL  : {user_data.get('html_url', 'N/A')}")


def main():
    """
    Main function to run the script.
    """

    username = input("Enter GitHub username: ").strip()

    if not username:
        print("Error: Username cannot be empty.")
        sys.exit(1)

    user_data = fetch_github_user(username)

    if user_data:
        display_user_summary(user_data)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
