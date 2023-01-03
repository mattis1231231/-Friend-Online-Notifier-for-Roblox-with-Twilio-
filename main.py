import requests
from twilio.rest import Client
import time
import time

# Replace these values with your own
ROBLOX_API_KEY = "your_roblox_api_key"
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"
DESTINATION_PHONE_NUMBER = "your_destination_phone_number"
FRIEND_USERNAME = "your_friend's_username"

# Set up the Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

headers = {"Authorization": f"Bearer {ROBLOX_API_KEY}"}

# Initialize the online status flag to False
is_online = False

# Run the code to check the online status and send the notification repeatedly
while True:
    # Get the user ID of the friend
    response = requests.get(
        f"https://api.roblox.com/users/get-by-username?username={FRIEND_USERNAME}",
        headers=headers)
    response.raise_for_status()
    friend_user_id = response.json()["Id"]

    # Check if the friend is online
    response = requests.get(
        f"https://api.roblox.com/users/{friend_user_id}/onlinestatus",
        headers=headers)
    response.raise_for_status()
    new_is_online = response.json()["IsOnline"]

    if new_is_online and not is_online:
        # The user has just gone online, send a notification via Twilio
        message = client.messages.create(
            body=f"{FRIEND_USERNAME} is now online on Roblox.",
            from_=TWILIO_PHONE_NUMBER,
            to=DESTINATION_PHONE_NUMBER)
        print(f"Sent notification: {message.sid}")
        is_online = True
    elif not new_is_online:
        # The user is not online, reset the online status flag
        is_online = False
        print(f"{FRIEND_USERNAME} is currently not online")
    else:
        # The user is still online
        print(f"{FRIEND_USERNAME} is still online")

    # Pause for one minute before checking again
    time.sleep(60)
