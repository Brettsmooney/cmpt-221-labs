#env FLASK_APP=part1.py flask run

from flask import Flask
from string import Template

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "<br><hr><center><h1>HOME PAGE</h1></center><hr>"

#static route
@app.route("/")
@app.route("/index")
def index():
    return "<br><hr><center><h1>INDEX PAGE</h1></center><hr>"

HTML_TEMPLATE = Template("<br><hr><center><h1> $egg , does this work? </h1></center><hr>")

#dynamic route
@app.route("/<variable>")
def dynamic(variable):
    return HTML_TEMPLATE.substitute(egg=variable)
