import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, escape
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'log in as %s' % escape(session['username'])
    else:
        return 'you are not logged in'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''<form action="" method="post">
              <p><input type=text name=username>
              <p><input type=submit value=login>
              </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run()