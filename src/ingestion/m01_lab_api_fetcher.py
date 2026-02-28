"""
Your Task:

Use the requests library to hit https://randomuser.me/api/.

Extract the email, city, and age from the JSON response.

The Engineering Twist: Wrap your code in a try...except block. What happens if your internet is off? What if the API is down? A "Leverage Engineer" handles the crash gracefully.

"""
import os
import time
import requests
import json

def fetch_random_user(retries=3, delay=2):
    url = "https://randomuser.me/api/"
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            user_info = data['results'][0]
            email = user_info['email']
            city = user_info['location']['city']
            age = user_info['dob']['age']
            return {
                'email': email,
                'city': city,
                'age': age
            }
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            attempt += 1
            if attempt < retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("All attempts failed. Please check your connection or the API status.")
    return None

def save_to_raw(data, folder="data/raw/", filename_prefix="random_user"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = f"{filename_prefix}_{int(time.time())}.json"
    filepath = os.path.join(folder, filename)
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filepath}")
    except Exception as e:
        print(f"Failed to save data: {e}")

if __name__ == "__main__":
    result = fetch_random_user()
    if result:
        save_to_raw(result)