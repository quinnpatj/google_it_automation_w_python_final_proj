#!/usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attach = None):
    # Generates email from report_email.py or health_check.py
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    # Generates attachment from report_email.py
    if attach != None:
        attach_fn = os.path.basename(attach)
        mime_type, _ = mimetypes.guess_type(attach)
        mime_type, mime_subtype = mime_type.split('/', 1)
        ap = open(attach, 'rb')
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=attach_fn)
    return message

def send_email(message):
    # Sends email
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()