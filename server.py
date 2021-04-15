from flask import Flask, request, render_template, url_for
from jinja2 import Template
import json
import os
import random

app = Flask(__name__)

@app.route('/')
def a():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/member')
def carousel():
    with open('templates/workers.json', encoding='utf-8') as file:
        data = json.load(file)
        worker = random.choice(data)
    return render_template('a.html', **worker)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')