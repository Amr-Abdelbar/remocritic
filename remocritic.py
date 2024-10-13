import datetime
import matplotlib as plt
import numpy as np
import flask
app = flask.Flask("RemoCritic")

def get_html(file_name):
    html_file = open(file_name + ".html")
    content = html_file.read()
    html_file.close()

@app.route("/")
def homepage():
    return get_html(index)