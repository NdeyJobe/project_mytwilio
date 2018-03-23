from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa71f866c339eb319a58b03c8bb0cb944"
# Your Auth Token from twilio.com/console
auth_token  = "6930b64e1e47ad4551fb15643a562293"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+xxxxxxxxxxx",
    from_="+xxxxxxxxxxx",
    body="Good luck at the embassy! Please come back to look at my code in the afternoon. This is an automated message.")

print(message.sid)
