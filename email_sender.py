# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# ../../../../../opt/homebrew/bin/python3.11 app_agent.py
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

example_email = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Delivery Attempt Failed - Action Needed</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 20px;">
    <table width="600" style="background-color: #ffffff; margin: auto; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <tr>
            <td style="text-align: center;">
                <h2 style="color: #333333;">🚚 Delivery Attempt Failed</h2>
            </td>
        </tr>
        <tr>
            <td>
                <p style="color: #555555;">Hello <strong>[Customer Name]</strong>,</p>

                <p style="color: #555555;">We attempted to deliver your package today but were unable to complete the delivery due to an incomplete address.</p>

                <ul style="color: #555555;">
                    <li><strong>Delivery Attempt ID:</strong> #48201923</li>
                    <li><strong>Scheduled Delivery Date:</strong> April 26, 2025</li>
                    <li><strong>Status:</strong> Action Required</li>
                </ul>

                <p style="text-align: center; margin: 30px 0;">
                    <a href="http://127.0.0.1:8001/" style="background-color: #007BFF; color: white; padding: 12px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Update Delivery Details</a>
                </p>

                <p style="color: #555555;">Failure to update your information may result in the package being returned to the sender.</p>

                <p style="color: #555555;">If you have already updated your information, please disregard this message.</p>

                <p style="color: #555555;">Thank you for choosing <strong>[Shipping Company Name]</strong>.</p>

                <hr style="margin: 20px 0; border: none; border-top: 1px solid #eeeeee;">

                <p style="color: #aaaaaa; font-size: 12px;">Shipping Support Team<br>
                Questions? Contact us at <a href="mailto:support@example.com" style="color: #007BFF;">support@example.com</a></p>
            </td>
        </tr>
    </table>
</body>
</html>
"""

example_email2 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Late Assignment Submission</title>
</head>
<body style="font-family: Arial, sans-serif; padding: 20px; background-color: #f9f9f9;">

                <p style="color: #333333;">Hi Professor,</p>

                <p style="color: #333333;">Sorry for the late submission. Here's the link to my assignment:</p>

                <p style="margin: 20px 0;">
                    <a href="https://example.com/assignment-upload" style="color: #007BFF;">View Assignment</a>
                </p>

                <p style="color: #333333;">Please let me know if there are any issues accessing it.</p>

                <p style="color: #333333;">Thank you,<br>[Student Name]</p>

</body>
</html>
"""
message = Mail(
    from_email='jamesb816438@outlook.com',
    to_emails='tstrzyz@uw.edu',
    subject='HIHIHIHIH PHISH  (not)',
    html_content=example_email2)
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
