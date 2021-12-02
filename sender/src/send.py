import argparse
import boto3
from dotenv import load_dotenv
import os

from aws.ses import send_raw_email
from messages import Message, MailBody, MailHeaders
from utils import open_html_file, open_json_file


load_dotenv()


def parse_arguments():
    parser = argparse.ArgumentParser(description='X')
    parser.add_argument('-H', '--html', required=True, help='')
    parser.add_argument('-r', '--recipients', required=True, help='')
    parser.add_argument('-c', '--context', help='')
    parser.add_argument('-s', '--subject', required=True, help='')
    return parser.parse_args()

def send_email(args):
    client = boto3.client('ses', 'eu-central-1')
    
    # recipients = Recipients()
    # recipients.add(open_json_file(args.recipients)[0]) # TODO: iter

    headers = MailHeaders()
    headers.set_sender(os.getenv('EMAIL_SENDER'))
    headers.set_subject(args.subject)
    headers.set_recipients(open_json_file(args.recipients)[0]) # TODO: iter

    body = MailBody()
    if args.context:
        body.set_context(open_json_file(args.context))
    body.set_contents(open_html_file(args.html))

    msg = Message(headers, body)
    send_raw_email(client, msg)


    # sender = EMAIL_SENDER
    # client = boto3.client('ses', 'eu-central-1')
    # recipients = _get_recipients(sys.argv[1])
    # html = open_html_file(sys.argv[2])
    # message = create_raw_message(sender, recipients, EMAIL_SUBJECT, html)
    # send_raw_email(client, sender, recipients, message)

if __name__ == '__main__':
    args = parse_arguments()
    send_email(args)