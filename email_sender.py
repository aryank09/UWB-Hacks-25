# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

message = Mail(
    from_email='jamesb816438@outlook.com',
    to_emails='tstrzyz@uw.edu',
    subject='HIHIHIHIH PHISH  (not)',
    html_content='<strong>Trololololo haha vs code</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
# send_email(subject, body, to_email, from_email,
#            from_password, smtp_server, smtp_port)
