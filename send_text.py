from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5551997211148", 
    from_="+554139075329",
    body="Ich liebe Dich! <3 Gui")

print(message.sid)
