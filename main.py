import os
import smtplib
import requests
from flask import Flask, render_template, request


MY_EMAIL = os.environ.get('own_email')  #own_email=aleshichevigor@outlook.com
PASSWORD = os.environ.get('own_password')   #'45rhfy7853rt' own_password=45rhfy7853rt
own_email = 'aleshichevigor@yahoo.com'  # baVZKzXntWYGnj3


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = requests.get(blog_url).json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for current_post in all_posts:
        if current_post['id'] == index:
            requested_post = current_post
    return render_template("post.html", post=requested_post )


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_emails( data['username'], data['email'], data['phone_number'], data['message'] )
        # name = data['username'],
        # email = data['email'],
        # phone = data['phone_number']
        # message = data['message']
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")


def send_emails(username, email, phone_number, message):
    """Send email if price low."""
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=own_email,
            msg=f"Subject:Hi \n\nName: {username}\nEmail: {email}\nPhone: {phone_number}\nMessage:{message}".encode('utf-8')
        )
    return print(f"Check your email: {email}")


if __name__ == "__main__":
    app.run(debug=True)

