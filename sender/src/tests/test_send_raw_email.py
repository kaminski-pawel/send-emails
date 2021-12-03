import base64
import unittest

from src.send import prepare_message


class PrepareMessageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.email_data = {
            'Context': {'variable': 'Variable: ZaĹĽĂłĹ‚Ä‡ gÄ™Ĺ›lÄ… jaĹşĹ„'},
            'Destinations': {
                'BccAddresses': [],
                'CcAddresses': [],
                'ToAddresses': ['some@example.com']},
            'Subject': 'ZaĹĽĂłĹ‚Ä‡ gÄ™Ĺ›lÄ… jaĹşĹ„'}
        self.html = '''<!DOCTYPE html>\n
        <html xmlns="http://www.w3.org/1999/xhtml"
              xmlns:v="urn:schemas-microsoft-com:vml" 
              xmlns:o="urn:schemas-microsoft-com:office:office"\n>
               <body> <div> <div> <table> <tbody> <tr> <td> <div> 
               <table> <tbody> <tr> <td> 
               <div>Zażółć gęślą jaźń</div>
               </td> </tr> </tbody> </table> </div> </td> </tr> </tbody> 
               </table> </div> </div> </body>\n</html>\n'''
        self.message = prepare_message(self.email_data, self.html)

    def _get_mail_body_from_message(self, value: str) -> str:
        return base64.b64decode(value
            .split('Content-Transfer-Encoding: base64\n\n')[-1] \
            .split('\n\n')[0]).decode('ansi')

    def test_list_receivers_to(self):
        self.assertTrue('some@example.com' in self.message.list_receivers('To'))
        self.assertEqual(1, len(self.message.list_receivers('To')))

    def test_headers_to(self):
        self.assertEqual('some@example.com', self.message['To'])

    def test_headers_subject(self):
        self.assertEqual('Zażółć gęślą jaźń', self.message['Subject'])

    def test_body(self):
        mail_body = self._get_mail_body_from_message(self.message.as_string())
        self.assertTrue('Zażółć gęślą jaźń' in mail_body)
