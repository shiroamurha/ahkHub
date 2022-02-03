from flask import Flask, jsonify, render_template, request
from buttons import *


app = Flask(__name__)

htmlsrc = open('index.html', 'r')
htmlsrc = htmlsrc.read()


@app.route('/')
def index():
    return f'{htmlsrc}'

@app.route('/button1on')
def button1_event_on():
    var = button1()
    var.run()
    return ''

@app.route('/button1off')
def button1_event_off():
    var = button1()
    var.exit()
    return ''