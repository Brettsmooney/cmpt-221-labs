#env FLASK_APP=bootstrap.py flask run

from flask import Flask
from string import Template
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    #flask looks in templates folder by default

# Run Flask Programmatically
if __name__ == "__main__":
    # Set Debug to true, set host IP to localhost, and set port to 80
    app.run(debug=True, host="127.0.0.1", port=80)
