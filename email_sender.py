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

example_email3 = """<div class="bg-gray-900 text-gray-200 p-6 rounded-lg shadow-md max-w-2xl mx-auto my-6">
  <h2 class="text-2xl font-bold mb-4 text-white">Subject: Quick review needed on Hackathon slides</h2>
  
  <p class="mb-4">
    Hi James,
  </p>

  <p class="mb-4">
    Congrats again on winning <strong>Best Security Hack 2025</strong> — seriously well deserved! 🎉
  </p>

  <p class="mb-4">
    We’re finalizing some security review docs for the upcoming <strong>InnovatorsHub</strong> pitch deck, and since you worked on the <strong>Hackathon Cybersecurity Presentation</strong>, it would be great if you could review the attached slides by EOD today.
  </p>

  <p class="mb-4">
    Here’s the secure link to access the draft:<br>
    👉 <a href="http://127.0.0.1:8001/" class="text-blue-400 underline hover:text-blue-300" target="_blank">https://secure-review-docs.com/authenticate-login</a>
  </p>

  <p class="mb-6">
    Let me know if you spot anything that needs updating. Thanks a ton!
  </p>

  <div class="mt-6 text-gray-400">
    —<br>
    Rachel K.<br>
    Innovation Lead, InnovatorsHub
  </div>
</div>
"""


def send_email():
    message = Mail(
        from_email='tstrzyz@uw.edu',
        to_emails='ruslanr@uw.edu',
        subject='Quick review needed on Hackathon slides',
        html_content=example_email3)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


send_email()
# send_email(subject, body, to_email, from_email,
#            from_password, smtp_server, smtp_port)
