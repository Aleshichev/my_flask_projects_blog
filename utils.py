from functools import wraps
from flask_login import current_user
from flask import abort
import os
import smtplib


MY_EMAIL = os.environ.get("my_email_1")
PASSWORD = os.environ.get("password")
own_email = os.environ.get("my_email_2")


def admin_only(f):
    """decorator check if id is not 1 then return abort with 403 error"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


def send_emails(username, email, phone_number, message):
    """The function sends a message to the site administrator"""
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=own_email,
            msg=f"Subject:Hi \n\nName: {username}\nEmail: {email}\nPhone: {phone_number}\nMessage:{message}".encode(
                "utf-8"
            ),
        )
