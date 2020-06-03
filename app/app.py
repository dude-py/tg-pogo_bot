# app/app.py
import os
from flask import url_for, send_from_directory
from manager import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
@app.route('/index.htm')
def index():
    """ Main page """
    return "Flask app working ok"


@app.route('/pogo_bot_enter_point', methods=['POST'])
def pogo_bot_enter_point():
    """ Точка входу для бота """
    pass
