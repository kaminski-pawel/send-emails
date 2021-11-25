def send_raw_email(client, sender, recipients, raw_message, config=''):
    client.send_raw_email(
            Source=sender,
            Destinations=recipients,
            RawMessage={'Data': raw_message},
            ConfigurationSetName=config)
