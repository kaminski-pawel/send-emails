from botocore.exceptions import ClientError


def send_raw_email(client, sender, recipients, raw_message):
    try:
        response = client.send_raw_email(
                Source=sender,
                Destinations=recipients,
                RawMessage={'Data': raw_message})
    except ClientError as e:
        _log(e.response['Error']['Message'])
    else:
        _log(f'Email sent. Message ID: {response["MessageId"]}'),

def _log(msg):
    print(msg)