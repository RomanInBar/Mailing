from smtplib import SMTP_SSL
from email.mime.text import MIMEText

from celery_ import clr, log
from logs.config import mailinglog


@clr.task(name='send_message')
def send_message(message: str, clients: list):
    log.info('Запуск send_message.')
    for client in clients:
        try:
            msg = MIMEText(message, 'html')
            msg['Subject'] = 'I do not know'
            msg['From'] = 'admin@mail.ru'
            msg['To'] = client
            port = 465
            server = SMTP_SSL('mail.privateemail.com', port)
            server.login('barabinr@list.ru', 'morfin532')
            result = server.send_message(msg)
            log.info('Сообщение отправлено')
            server.quit()
        except Exception as e:
            log.info(f'Произошла ошибка {e}')
            return e
        log.info('Сообщения отправлены.')
        return result
