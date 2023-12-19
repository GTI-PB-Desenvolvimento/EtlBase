import smtplib
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


@dataclass
class SMTPConfig:
    host: str
    port: int
    email: str
    password: str

@dataclass
class MailMessage:
    subject: str
    toaddrs: list[str]
    text: MIMEText
    atachments: list[MIMEBase]


class SMTPMail:
    def __init__(self, smtp_config: SMTPConfig):
        self.mail_config = smtp_config

    def _send(self, msg: MIMEMultipart):
        with smtplib.SMTP(self.mail_config.host, self.mail_config.port) as server:
            server.starttls()
            server.login(self.mail_config.email, self.mail_config.password)
            server.send_message(msg)

    def send(self, message: MailMessage):
        msg = MIMEMultipart()
        msg['From'] = self.mail_config.email 
        msg['To'] = message.toaddrs
        msg['Subject'] = message.subject

        for attachment in [message.text, *message.atachments]:
            msg.attach(attachment) 

        self._send(msg)
