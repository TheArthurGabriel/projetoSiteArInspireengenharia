from flask import Flask, render_template

from configuration import configure_all

app = Flask(__name__)

configure_all(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)


