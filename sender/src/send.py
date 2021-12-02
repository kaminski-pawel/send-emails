import argparse
import boto3
from dotenv import load_dotenv
import os
import sys

# from aws.ses import send_raw_email
# from msg import create_raw_message
# from utils import open_csv_file, open_html_file
# def _get_recipients(arg):
#     return open_csv_file(arg) if os.path.isfile(arg) else [arg]


load_dotenv()
EMAIL_SENDER = os.getenv('EMAIL_SENDER')



def parse_arguments():
    parser = argparse.ArgumentParser(description='X')
    parser.add_argument('-H', '--html', required=True, help='')
    parser.add_argument('-r', '--recipients', required=True, help='')
    parser.add_argument('-c', '--context', help='')
    parser.add_argument('-s', '--subject', required=True, help='')
    return parser.parse_args()

def send_email(args):
    print('args', args)
    print('EMAIL_SENDER', EMAIL_SENDER)
    pass
    # sender = EMAIL_SENDER
    # client = boto3.client('ses', 'eu-central-1')
    # recipients = _get_recipients(sys.argv[1])
    # html = open_html_file(sys.argv[2])
    # message = create_raw_message(sender, recipients, EMAIL_SUBJECT, html)
    # send_raw_email(client, sender, recipients, message)

if __name__ == '__main__':
    args = parse_arguments()
    send_email(args)