# coding=utf-8
from config import config
from utils import dbhelper
from datetime import datetime

def login(username, password):
  admins = config['administrators']

  if username not in admins:
    raise Exception('账号或密码不匹配')

  user_info = admins[username]

  if password != user_info['password']:
    raise Exception('账号或密码不匹配')

  return user_info

def all():
  sql = """
    select * 
    from users
    where deletedAt is null
  """
  return dbhelper.execute_query(sql)

def get(phone):
  sql = """
    select * 
    from users 
    where phone = %s
  """
  return dbhelper.execute_query(sql, params=(phone), single=True)

def add(region, phone, password, salt, nickname, userRole):
  sql = """
    insert into users(
      region,
      phone,
      nickname,
      passwordHash,
      passwordSalt,
      groupCount,
      timestamp,
      userRole,
      createdAt,
      updatedAt
    )
    values(
      %s,
      %s,
      %s,
      %s,
      %s,
      %d,
      %d,
      %d,
      %s,
      %s
    )
  """

  dbhelper.execute_update(sql,(
    region,
    phone,
    nickname,
    password,
    salt,
    0,
    0,
    int(userRole),
    datetime.now(),
    datetime.now()
  ))

def delete(phone):
  sql = """
    update users
    set
      updatedAt = %s,
      deletedAt = %s
    where phone = %s
  """

  dbhelper.execute_update(sql, params=(
    datetime.now(),
    datetime.now(),
    phone
  ))

def reset_password(phone, password, salt):
  sql = """
    update users
    set
      passwordHash=%s,
      passwordSalt=%s,
      updatedAt = %s 
    where phone = %s
  """

  dbhelper.execute_update(sql, params=(
    password,
    salt,
    datetime.now(),
    phone
  ))

def set_userrole(phone, userRole):
  sql = """
    update users
    set
      userRole=%s,
      updatedAt = %s 
    where phone = %s
  """

  dbhelper.execute_update(sql, params=(
    userRole,
    datetime.now(),
    phone
  ))
