#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/28 11:00

from hashlib import sha256
from hmac import HMAC
import os

def hash_password(password, salt = None):
    if isinstance(password, unicode):
        password = password.encode('UTF-8')
    if salt is None:
        salt = os.urandom(8)
    result = HMAC(password, salt, sha256).digest()
    return result,salt

def authen_password(result, new_password, salt):
    return hash_password(new_password,salt)[0] == result

if __name__ == '__main__':
    password = raw_input('please input the password: ')
    result,salt = hash_password(password)
    print result
    new_password = raw_input('please input the password again: ')
    print authen_password(result,password,salt)
