# Friend-Online-Notifier-for-Roblox-with-Twilio
The Friend Online Notifier for Roblox with Twilio is a Python script intended to send an SMS notification to a specific phone number when a specific friend of the user comes online on Roblox.

The script uses the Roblox API and the Twilio API to check the friend's online status and to send the notification. The user must provide a valid Roblox API key and Twilio API data in the script variables to use the script.

The script starts by setting up the Twilio client using the recommended TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN. Then the friend's online status is queried using the Roblox API and the assumed FRIEND_USERNAME. If the friend is online and the online status flag has not yet been set, an SMS notification is sent to the assumed DESTINATION_PHONE_NUMBER via the Twilio client. If the friend is not online, the online status will be reset.

The script will then continue to check the friend's online status and the notifications that are sent, with a one-minute pause between each check. This process continues until the script is stopped.
