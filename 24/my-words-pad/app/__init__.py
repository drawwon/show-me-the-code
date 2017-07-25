#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 9:47

from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object("config")

db = MongoEngine(app)

import views,models