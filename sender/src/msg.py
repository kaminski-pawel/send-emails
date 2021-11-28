from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_raw_message(sender, recipients, subject, html):
    msg = MIMEMultipart('mixed')
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    msg['Subject'] = Header(subject, 'utf-8')

    msg_body = MIMEMultipart('alternative')
    msg_body.attach(MIMEText(html.encode('ansi'), 'html', 'utf-8'))
    msg.attach(msg_body)
    # TODO: attachments
    # from email.mime.application import MIMEApplication
    # attachment_msg = MIMEApplication(attachment)
    # attachment_msg.add_header('Content-Disposition', 'attachment', filename=attachment_filename)
    # msg.attach(attachment_msg)
    return msg.as_string()