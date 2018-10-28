# coding=utf-8
from config import config
from utils import dbhelper

def login(username, password):
  admins = config['administrators']

  if username not in admins:
    raise Exception('账号或密码不匹配')

  user_info = admins[username]

  if password != user_info['password']:
    raise Exception('账号或密码不匹配')

  return user_info

def all():
  sql = 'select * from users'
  return dbhelper.execute_query(sql)