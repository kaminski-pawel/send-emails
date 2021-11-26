import boto3
from dotenv import load_dotenv
import os
import sys

from aws.ses import send_raw_email
from msg import create_raw_message
from utils import open_csv_file, open_html_file


load_dotenv()

EMAIL_SUBJECT = 'Zażółć gęślą jaźń'
EMAIL_SENDER = os.getenv('EMAIL_SENDER')

def _get_recipients(arg):
    return open_csv_file(arg) if os.path.isfile(arg) else [arg]

def send_email():
    sender = EMAIL_SENDER
    client = boto3.client('ses', 'eu-central-1')
    recipients = _get_recipients(sys.argv[1])
    html = open_html_file(sys.argv[2])
    message = create_raw_message(sender, recipients, EMAIL_SUBJECT, html)
    send_raw_email(client, sender, recipients, message)

if __name__ == '__main__':
    send_email()