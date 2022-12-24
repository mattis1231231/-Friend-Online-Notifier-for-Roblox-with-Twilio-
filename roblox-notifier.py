import requests

# Replace YOUR_ROBLOX_API_KEY with your actual Roblox API key
roblox_api_key = "YOUR_ROBLOX_API_KEY"

# Replace YOUR_FRIEND_USERNAME with the actual username of the friend you want to track
friend_username = "YOUR_FRIEND_USERNAME"

# Get the user ID of the friend
response = requests.get(f"https://users.roblox.com/v1/users/by-username/{friend_username}", headers={"Authorization": f"Bearer {roblox_api_key}"})

# Check the response status code
if response.status_code == 200:
    # Get the user ID of the friend
    friend_id = response.json()["id"]

    # Get a list of the friend's friends
    response = requests.get(f"https://friends.roblox.com/v1/users/{friend_id}/friends", headers={"Authorization": f"Bearer {roblox_api_key}"})

    # Check the response status code
    if response.status_code == 200:
        # Get the list of friends
        friends = response.json()["data"]

        # Find the specific friend in the list
        for friend in friends:
            if friend["username"] == friend_username:
                # Check if the friend is online
                if friend["isOnline"]:
            # Send a notification using Twilio
            # Replace YOUR_TWILIO_API_KEY, YOUR_TWILIO_API_SECRET, YOUR_TWILIO_PHONE_NUMBER, and
