# coding=utf-8
config = {
  'db': {
    'host': 'localhost',
    'port': 3306,
    'username': 'root',
    'password': 'aa123123',
    'dbname': 'sealtalk'
  },
  'administrators': {
    'admin': {
      'username': 'admin',
      'password': 'aa123123',
      'role_type': 99999
    }
  },
  'auth_exclusive': [
    '/login',
    '/favicon.ico'
  ]
}