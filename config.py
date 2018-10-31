# coding=utf-8
config = {
  # 数据库相关配置
  'db': {
    'host': 'localhost',
    'port': 3306,
    'username': 'root',
    'password': 'aa123123',
    'dbname': 'sealtalk'
  },
  # 管理员账号配置
  'administrators': {
    'admin': {
      'username': 'admin',
      'password': 'aa123123',
      # 超级管理员默认type为99999, 暂时无用,后期扩展用
      'role_type': 99999
    }
  },
  # 不需要登录权限的地址配置
  'auth_exclusive': [
    '/login',
    '/favicon.ico'
  ]
}