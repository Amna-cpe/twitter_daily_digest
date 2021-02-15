from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from tw import create_twitter_digest


CLIENT_SECRET_FILE = 'clieny_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.readonly']


create_twitter_digest()

with open('test.html', 'r') as f:
    html_content = f.read()
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


msg = EmailMessage()
msg['to'] = 'amna.the.nerdy@gmail.com'
msg['subject'] = 'Your daily digest'
msg.set_content("html_content")
html_page = open('test.html').read()
msg.add_alternative( html_page , subtype='html')
raw_string = base64.urlsafe_b64encode(msg.as_bytes()).decode()
message = service.users().messages().send(
    userId = 'me', body = {'raw':raw_string}).execute()
