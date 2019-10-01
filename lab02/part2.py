#env FLASK_APP=part2.py flask run

from flask import Flask
from string import Template
from flask import render_template

app = Flask(__name__)

#static route
@app.route("/")
@app.route("/index")
def index():
    return render_template('digitalResumeIndex.html')
    #flask looks in templates folder by default

@app.route("/resume")
def hello():
    return render_template('digitalResume.html')
