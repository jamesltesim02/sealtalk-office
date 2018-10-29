# coding=utf-8
import pymysql
from config import config

def execute_update(sql, params=None):
  db_conf = config['db']
  db = pymysql.connect(
    db_conf['host'],
    db_conf['username'],
    db_conf['password'],
    db_conf['dbname']
  )
  # 使用cursor()方法获取操作游标 
  cursor = db.cursor()

  try:
    # 执行sql语句
    cursor.execute(sql, params)
    # 执行sql语句
    db.commit()
  except Exception as e:
    # 发生错误时回滚
    db.rollback()
    raise e
  finally:
    cursor.close()
    # 关闭数据库连接
    db.close()

def execute_query(sql, params=None, single=False):
  result = []

  db_conf = config['db']
  db = pymysql.connect(
    db_conf['host'],
    db_conf['username'],
    db_conf['password'],
    db_conf['dbname']
  )

  try:
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    # 执行SQL语句
    cursor.execute(sql, params)
    if single:
      return cursor.fetchone()
    # 获取所有记录列表
    return cursor.fetchall()
  except:
    pass
  finally:
    cursor.close()
    db.close()

  return result
