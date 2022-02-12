#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attach, title, body):
    # Generates PDF from text formatted in report_email.py
    report = SimpleDocTemplate(attach)
    styles = getSampleStyleSheet
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body, styles["BodyText"])
    br = Spacer(1,20)
    report.build([report_title, br, report_body, br])