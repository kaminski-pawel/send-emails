from bs4 import BeautifulSoup
from jinja2 import Template
from typing import Dict


class HtmlIsNotSetException(Exception): pass


class MailBody:
    def __init__(self):
        self._context = {}
        self._soup = None
        self._text_part = None
        self._html_part = None
        self._encoding = 'ansi'

    def set_context(self, value: Dict[str, str]) -> None:
        self._context = value

    def set_contents(self, html: str) -> None:
        self._set_html(html)
        self._set_text()

    def _set_html(self, value: str) -> None:
        self._html_part = Template(value).render(**self._context)
    
    def to_html(self) -> str:
        return self._html_part

    def to_bytes_html(self) -> bytes:
        return self.to_html().encode(self._encoding)

    def _set_text(self) -> None:
        if self._html_part is None:
            raise HtmlIsNotSetException('Html must be set before text part. ' \
                                        'Run set_html(_html) first.')
        _soup = BeautifulSoup(self._html_part, 'html.parser')
        self._text_part = _soup.get_text().strip()

    def to_text(self) -> str:
        return self._text_part

    def to_bytes_text(self) -> str:
        return self.to_text().encode(self._encoding)