# coding=utf-8
from flask import Blueprint, render_template, abort, request, session
import json
from model import user as userModel

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/user')
def user_index():
  user_list = userModel.all()
  user_info = session["loged_user"]
  print(user_list)
  return render_template('user.html', users = user_list, user = user_info)

@user.route('/login')
def login():
  return render_template('login.html')

@user.route('/login', methods=['POST'])
def doLogin():
  username, password = request.form['username'], request.form['password']
  try:
    user_info = userModel.login(username, password)
    session["loged_user"] = user_info

    return json.dumps({
      'status': 200,
      'msg': 'OK',
      'data': user_info
    })
  except Exception as e:
    print(e)
    return json.dumps({
      'status': -1,
      'msg': e.message
    })