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
    var = button('textbox.exe')
    var.run()
    return ''

@app.route('/button1off')
def button1_event_off():
    var = button('textbox.exe')
    var.exit()
    return ''

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000)