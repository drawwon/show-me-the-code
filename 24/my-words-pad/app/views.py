#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 9:52

from . import app
from flask import render_template,request
from models import Words
from datetime import datetime

@app.route('/')
def index():
    words = Words.objects.all()
    return render_template('index.html', words=words)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get("name")
    content = request.form.get("content")
    time = datetime.now()
    words = Words(content=content,name=name, time =time)
    words.save()
    words = Words.objects.order_by('-time')
    return render_template('index.html', words=words)