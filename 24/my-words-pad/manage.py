#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/24 10:32

from flask_script import Manager,Server
from app import app
from app.models import Words

manager = Manager(app)
manager.add_command('runserver',Server(host='0.0.0.0',port=5000,use_debugger=True))

@manager.command
def save_word():
    words = Words(name='wz11',content='this is first words')
    words.save()

if __name__ == '__main__':
    manager.run()