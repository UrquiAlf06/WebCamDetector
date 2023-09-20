import smtplib
import imagesize
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()


def send_emaiL(image_path):
    email_user = os.getenv('email_user')
    password_user = os.getenv('gmail_key')
    email_message = EmailMessage()
    email_message["Subject"] = "New opp showed up!"
    email_message.set_content("Hey, I just captured a new person!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype="png")

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(email_user, password_user)
    gmail.sendmail(email_user, email_user, email_message.as_string())
    gmail.quit()

