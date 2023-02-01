from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from random import choice
import string


app = Flask(__name__)
app.secret_key = "gjskdhgodhgos"
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# Setting up db as class
class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=False)
    short_url = db.Column(db.String(), nullable=False, unique=True)

    def __init__(self, url, short_url):
        self.url = url
        self.short_url = short_url

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        print(url)
        if not url=="":
            db_url = db.session.query(Urls).filter_by(url=url).first()
            if db_url:
                result = f'http://127.0.01:5000/{db_url.short_url}'
                return render_template('index.html', result=result, link=url)
            else:
                short_url = generate_short_url(8)
                new_link = Urls(url, short_url)
                db.session.add(new_link)
                db.session.commit()
                result = f'http://127.0.01:5000/{short_url}'
                return render_template('index.html', result=result, link=url)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    link = db.session.query(Urls).filter_by(short_url=short_url).first()
    if link:
        print(link.url)
        return redirect(link.url)
    else:
        flash("Invalid URL")
        return render_template('index.html')


def generate_short_url(num):
    while True:
        key = ''.join(choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in range(num))
        db_short_url = db.session.query(Urls).filter_by(short_url = key).first()
        if not db_short_url:
            return key


# 404 page not round 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)