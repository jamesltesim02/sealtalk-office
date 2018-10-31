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

def all(keyword='', userRole='all', page=1, row_num=10):
  sql = """
    select * 
    from users
    where 
      deletedAt is null
  """
  count_sql = """
    select count(1) as data_count
    from users
    where 
      deletedAt is null
  """

  params = []
  if keyword:
    sql += ' and (phone like %s or nickname like %s)'
    count_sql += ' and (phone like %s or nickname like %s)'
    params.append('%' + keyword + '%')
    params.append('%' + keyword + '%')

  if userRole != 'all':
    sql += ' and userRole = %s'
    count_sql += ' and userRole = %s'
    params.append(userRole)

  sql += (' order by createdAt desc limit %s, %s' % (((page - 1) * row_num), row_num))

  count = dbhelper.execute_query(count_sql, params, single=True)['data_count']
  result = dbhelper.execute_query(sql, params)

  return {
    'count': count,
    'page': page,
    'row_num': row_num,
    'page_count': int((count + row_num - 1) / row_num),
    'data': result
  }

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
      '%s',
      '%s',
      '%s',
      '%s',
      '%s',
      %d,
      %d,
      %d,
      '%s',
      '%s'
    )
  """ % (
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
  )

  dbhelper.execute_update(sql)

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
