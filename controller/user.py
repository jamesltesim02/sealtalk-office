# coding=utf-8
from flask import Blueprint, render_template, abort, request, session
import json
from model import user as userModel

user = Blueprint('user', __name__, template_folder='templates')

default_password = '540e7ddab8d9256a1853ce5da115ecfc861b5364'
default_salt = '4943'

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

@user.route('/user')
def user_index():
  (
    keyword,
    page,
    userRole
  ) = (
    request.args.get('keyword'),
    request.args.get('page'),
    request.args.get('userRole') or 'all'
  )
  user_result = userModel.all(keyword, userRole, int(page or '1'))
  return render_template('user.html', users = user_result)

@user.route('/user', methods=['POST'])
def add():
  (
    phone,
    nickname,
    userRole
  ) = (
    request.form['phone'],
    request.form['nickname'],
    request.form['userRole']
  )

  userinfo = userModel.get(phone)
  
  if userinfo:
    return json.dumps({
      'status': -1,
      'msg': '账号已存在'
    })

  try:
    userModel.add(
      '86',
      phone,
      default_password,
      default_salt,
      nickname,
      userRole
    )
    return json.dumps({
      'status': 200,
      'msg': 'OK'
    })

  except Exception as e:
    print(e)
    return json.dumps({
      'status': -1,
      'msg': e.message
    })

@user.route('/user/<phone>', methods=['DELETE'])
def delele(phone):
  try:
    userModel.delete(phone)
    return json.dumps({
      'status': 200,
      'msg': 'OK'
    })
  except Exception as e:
    print(e)
    return json.dumps({
      'status': -1,
      'msg': e.message
    })

@user.route('/user/resetpass', methods=['POST'])
def resetpass():
  phone = request.form['phone']
  try:
    userModel.reset_password(phone, default_password, default_salt)
    return json.dumps({
      'status': 200,
      'msg': 'OK'
    })
  except Exception as e:
    print(e)
    return json.dumps({
      'status': -1,
      'msg': e.message
    })

@user.route('/user/setrole', methods=['POST'])
def setrole():
  phone, userRole = request.form['phone'], request.form['userRole']
  try:
    userModel.set_userrole(phone, userRole)
    return json.dumps({
      'status': 200,
      'msg': 'OK'
    })
  except Exception as e:
    print(e)
    return json.dumps({
      'status': -1,
      'msg': e.message
    })
