from email.header import Header
from typing import Dict, List, Union


class MailHeaders:
    """
    Email headers representation
    https://www.iana.org/assignments/message-headers/message-headers.xhtml
    """
    def __init__(self) -> None:
        self._headers = {}
        self._encoding = 'utf-8'

    def __getitem__(self, key: str) -> Union[str, List[str]]:
        return self._headers[key]

    def __iter__(self):
        return iter(self._headers)

    def items(self):
        return self._headers.items()

    def set_sender(self, value: str) -> None:
        self._headers['From'] = value

    def set_recipients(self, _recipients: Dict[str, List[str]]) -> None:
        self._headers['To'] = ','.join(_recipients['ToAddresses'])

    def set_subject(self, value: str) -> None:
        encoded_val = value.encode('ansi').decode('utf-8')
        self._headers['Subject'] = Header(encoded_val, self._encoding)
