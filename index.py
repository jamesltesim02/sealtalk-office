# coding=utf-8
from flask import Flask, render_template, request, session, redirect
from controller.common import common
from controller.user import user
from config import config
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__,static_folder='assets')
app.secret_key = b'_5#y2L"Faa4Q8z\n\xec]/'

app.register_blueprint(common)
app.register_blueprint(user)

@app.before_request
def authCheck():
  url = request.path
  
  if 'loged_user' in session:
    return
  
  if url.startswith('/assets'):
    return
  
  if url in config['auth_exclusive']:
    return
  
  return redirect('/login')

if __name__ == '__main__':
  app.run('localhost', 5000, debug=True)