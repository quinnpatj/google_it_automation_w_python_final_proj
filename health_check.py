#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os

def cpu():
    # Gets current CPU usage
    cpu_usage = psutil.cpu_percent(1)
    print(cpu_usage)
    return cpu_usage

def disk_space():
    # Gets current available disk space
    usage = shutil.disk_usage('/')
    percent_free = usage.free / usage.total * 100
    return percent_free

def memory():
    # Gets current free memory
    mem_free = psutil.virtual_memory().available
    mem_MB = mem_free / 1024 ** 2
    return mem_MB

def hostname():
    # Gets IP for localhost
    ip = socket.gethostbyname('localhost')
    return ip

def email(subject):
    # Sends email alert if conditions below are met
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)

if cpu() > 80:
    # Generates alert if current CPU usage is over 80%
    subject = "Error - CPU usage is over 80%"
    email(subject)

if disk_space() < 20:
    # Generates alert if less than 20% disk space is available
    subject = "Error - Available disk space is less than 20%"
    email(subject)

if memory() < 500:
    # Generates alert if available memory is less than 500MB
    subject = "Error - Available memory is less than 500MB"
    email(subject)

if hostname() != "127.0.0.1":
    # Generates alert if localhost's IP is not 127.0.0.1
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    email(subject)