#env FLASK_APP=part1.py flask run

from flask import Flask
from string import Template
from flask import render_template

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "<br><hr><center><h1>HOME PAGE</h1></center><hr>"

#static route
@app.route("/")
@app.route("/index")
def index():
    return "<body><br><hr><center><h1>INDEX PAGE</h1></center><hr><br><center><a href='/about'>about</a></center></body>"

@app.route("/about")
def hello():
    return "<br><hr><center><h1>ABOUT PAGE</h1></center><hr><br><center><a href='/index'>index</a></center><hr>"

#HTML_TEMPLATE = Template("<br><hr><center><h1> $egg , does this work? </h1></center><hr><br><center><a href='/about'>about</a></center><hr><br><center><a href='/index'>index</a></center><hr>")

#dynamic route
@app.route("/name/<variable>")
def dynamic(variable=None):
    return render_template('dynamic.html', variable=variable)

#dynamic route
#@app.route("/name/<variable>")
#def dynamic(variable):
#    return HTML_TEMPLATE.substitute(egg=variable)
