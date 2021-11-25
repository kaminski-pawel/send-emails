import boto3
from dotenv import load_dotenv
import os
import sys

from aws.ses import send_raw_email
from msg import create_raw_message
from utils import open_html_file

load_dotenv()

EMAIL_SUBJECT = ''
EMAIL_SENDER = os.getenv('EMAIL_SENDER')


def send_email():
    sender = sys.argv[1]
    recipients = [sys.argv[2]]
    client = boto3.client('ses', 'eu-central-1')
    html = open_html_file(sys.argv[3])
    message = create_raw_message(sender, recipients, EMAIL_SUBJECT, html)
    send_raw_email(client, sender, recipients, message)

if __name__ == '__main__':
    send_email()