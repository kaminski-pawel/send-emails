from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SUBJECT = 'Mail Test'
BODY = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>"""


def create_raw_message(sender, recipients):
    msg = MIMEMultipart('mixed')
    msg['From'] = sender
    msg['To'] = recipients[0] # what is the syntax for multiple recipients?
    msg['Subject'] = SUBJECT

    msg_body = MIMEMultipart('alternative')
    msg_body.attach(MIMEText(BODY, 'html', 'utf-8'))
    msg.attach(msg_body)
    # TODO: attachments
    # from email.mime.application import MIMEApplication
    # attachment_msg = MIMEApplication(attachment)
    # attachment_msg.add_header('Content-Disposition', 'attachment', filename=attachment_filename)
    # msg.attach(attachment_msg)
    return msg.as_string()