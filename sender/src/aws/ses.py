from botocore.client import BaseClient
from botocore.exceptions import ClientError
from typing import Any

from messages import Message


def send_raw_email(client: BaseClient, message: Message) -> None:
    try:
        response = client.send_raw_email(
                Source=message['From'],
                Destinations=message['To'].split(','),
                # Destinations=message['To'],
                RawMessage={'Data': message.as_string()})
    except ClientError as e:
        _log(e.response['Error']['Message'])
    else:
        _log(f'Email sent. Message ID: {response["MessageId"]}'),

def _log(msg: Any) -> None:
    print(msg)