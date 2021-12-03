import argparse
import boto3
from dotenv import load_dotenv
import os

from aws.ses import send_raw_email
from messages import Message, MailBody, MailHeaders
from utils import open_html_file, open_json_file


load_dotenv()
HELP_TEXT = 'Send many html emails customized to different recipients.'


def parse_arguments():
    parser = argparse.ArgumentParser(description=HELP_TEXT)
    parser.add_argument('-H', '--html', metavar='', required=True,
        help='Point to an html file to send.')
    parser.add_argument('-c', '--options', metavar='', default='options.json',
        help='Indicate json file with options (default: options.json).')
    return parser.parse_args()

def send_emails(args):
    for email_data in open_json_file(args.options):
        send_email(args, email_data)

def send_email(args, email_data):
    headers = MailHeaders()
    headers.set_sender(os.getenv('EMAIL_SENDER'))
    headers.set_subject(email_data['Subject'])
    headers.set_recipients(email_data['Destinations'])

    body = MailBody()
    body.set_context(email_data['Context'] or {})
    body.set_contents(open_html_file(args.html))

    message = Message(headers, body)
    send_raw_email(boto3.client('ses', 'eu-central-1'), message)


if __name__ == '__main__':
    args = parse_arguments()
    send_emails(args)