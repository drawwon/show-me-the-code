#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/29 11:02

from flask import Flask


app = Flask(__name__)
@app.route('/')
def index_page():
    return 'index'

@app.route('/hello')
def hello_world():
    return 'hello'

if __name__ == '__main__':
    app.debug = True
    app.run()