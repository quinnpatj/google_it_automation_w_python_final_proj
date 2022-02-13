#!/usr/bin/env python3

import os
import datetime
import reports
import emails

# Gets current date
date = datetime.datetime.now().strftime('%Y-%m-%d')

def process_text(path):
    # Iterates over files in directory and formats text
    processed = ""
    for file in os.listdir(path):
        if file.endswith(".txt"):
            f = open(path + file)
            val = f.readlines()
            name = val[0]
            weight = val[1]
            processed += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    return processed

if __name__ == "__main__":
    # Generates PDF from formatted text
    path = 'supplier-data/descriptions/'
    attach = "/tmp/processed.pdf"
    title = "Process Updated on " + date
    body = process_text(path)
    reports.generate_report(attach, title, body)

    # Sends email with PDF attachment
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, recipient, subject, body, attach)
    emails.send_email(message)