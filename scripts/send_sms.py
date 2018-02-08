"""
Kaitlyn's script will parse the received SMS that came in through receive_sms.py, then send
it to our Slack bot by calling this script with the Slack phone number and whatever message
needs to be sent.
"""

import re
import os

import click
from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('TWILIO_PHONE_NUMBER')

PHONE_NUMBER_RE = re.compile(r'^\+1\d{10}$')
PHONE_NUMBER_EXAMPLE = '+161723351010'

@click.command()
# When running this from terminal, follow run command with these arguments
@click.argument('to_number')
@click.argument('message_body', default='hello')

def send_sms_message(to_number, message_body):
    assert PHONE_NUMBER_RE.match(to_number), 'Phone number must match ' + PHONE_NUMBER_EXAMPLE
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to=to_number,
        from_=from_number,
        body=message_body)

if __name__ == '__main__':
    send_sms_message()