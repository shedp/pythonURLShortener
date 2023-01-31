from flask import Flask, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# import hashlib
from random import choice
import string


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    short_url = db.Column(db.String())

    def __init__(self, url, short_url):
        self.url = url
        self.short_url = short_url

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # POST METHOD which calls function on the URL entered
        url = request.form.get('url')
        short_url = shorten_url(url)
        return render_template('index.html', result = short_url)
    else:
        return render_template('index.html')


def short_url_id(long_url):
    # base62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # hash_value = int(hashlib.sha256(long_url.encode()).hexdigest(), 16)
    # hash_string = ""
    # url_length = len(long_url)
    # while url_length > 0:
    #     hash_string += base62[int(url_length) % 62]
    #     url_length /=62
    # return hash_string
    return ''.join(choice(string.scii_letters+string.digits) for _ in range(10))

# generate_short_id("https://www.enjoyalgorithms.com/blog/design-a-url-shortening-service-like-tiny-url")


if __name__ == "__main__":
    app.run(debug=True)