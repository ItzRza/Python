import smtplib
import customtkinter as CTk
from email.message import EmailMessage

from_mail = "rza62212@gmail.com"
app_password = "qupm bpqz fizm gofw"

def send_mail(header, content, to):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = header
    msg["From"] = from_mail
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_mail, app_password)
        server.send_message(msg)

    print("Sent!")


def create_file(name):
    with open(name, "a", encoding="utf-8") as f:
        pass

def check(name, line):
    with open(name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return lines[line]
    



