from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any

from .body import MailBody
from .headers import MailHeaders


class Message:
    """email.EmailMessage representation"""
    
    def __init__(self, headers: MailHeaders, body: MailBody) -> None:
        self.encoding = 'utf-8'
        self.headers = headers
        self.body = body
        self.msg = self._get_email_message()
        self._attach_email_body()

    def __getitem__(self, key) -> Any:
        return self.msg[key]

    def _get_email_message(self) -> MIMEMultipart:
        msg = MIMEMultipart('mixed')
        msg['From'] = self.headers['From']
        msg['To'] = self.headers['To']
        msg['Subject'] = self.headers['Subject']
        return msg

    def _attach_email_body(self) -> None:
        msg_body = MIMEMultipart('alternative')
        msg_body.attach(self._get_text_part())
        msg_body.attach(self._get_html_part())
        self.msg.attach(msg_body)

    def _get_html_part(self) -> MIMEText:
        return MIMEText(self.body.to_bytes_html(), 'html', self.encoding)

    def _get_text_part(self) -> MIMEText:
        return MIMEText(self.body.to_bytes_text(), 'plain', self.encoding)

    def as_string(self) -> str:
        return self.msg.as_string()