from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC486ef4f5d0ee7102d5afb710427c75ea"
# Your Auth Token from twilio.com/console
auth_token  = "08c5973b02ab26dfd09db5a0f32f1172"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918420341555", 
    from_="+12569077150",
    body="Hello from Python! My name is Suvro Banerjee.")

print(message.sid)
