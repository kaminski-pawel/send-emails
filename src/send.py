import boto3
import sys

from aws.ses import send_raw_email
from msg import create_raw_message


def send_email():
    sender = sys.argv[1]
    recipients = [sys.argv[2]]
    client = boto3.client('ses', 'eu-central-1')
    message = create_raw_message(sender, recipients)
    send_raw_email(client, sender, recipients, message)

if __name__ == '__main__':
    send_email()