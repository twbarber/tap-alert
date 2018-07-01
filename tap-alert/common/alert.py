from twilio.rest import Client


def send_as_sms(message, sender, recipients, account_sid, auth_token):
    client = Client(account_sid, auth_token)
    for recipient in recipients:
        message = client.messages.create(
            to=str(recipient),
            from_=str(sender),
            body=message
        )
