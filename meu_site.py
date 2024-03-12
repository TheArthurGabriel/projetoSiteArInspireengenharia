import os
from flask import Flask, render_template, request, session
from configuration import configure_all
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.getenv('APP_PASS')

configure_all(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login/page")
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['post'])
def login():
    data = request.form
    load_dotenv()
    if data['user'] == os.getenv('ADM_USER') and data['senha'] == os.getenv('ADM_PASSWORD'):
        session['username'] = data['user']
        return render_template('form.html')
    else:
        return render_template('login.html')

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


