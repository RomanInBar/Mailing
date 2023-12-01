import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

from celery_ import clr

load_dotenv('.env')

SMPT_HOST = os.getenv('SMPT_HOST')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
SMTP_USER = os.getenv('SMTP_USER')


def get_email_template(message, client):
    email = EmailMessage()
    email['Subject'] = 'Auto-Mailing'
    email['To'] = SMTP_USER
    email['From'] = SMTP_USER
    email.set_content(
        '<div>'
        f'Сообщение пользователю с адресом: {client}'
        '<br>'
        f'{message}'
        '</div>',
        subtype='html',
    )
    return email


@clr.task(name='send_message')
def send_message(message, client):
    email = get_email_template(message, client)
    with smtplib.SMTP_SSL(SMPT_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
