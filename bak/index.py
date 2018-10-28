#! /usr/bin/env python
# coding=utf-8

from flask import Flask
from flask_admin import Admin, BaseView, expose

app = Flask(__name__)
admin = Admin(app, name='sealtalk office', template_mode='bootstrap3')

class UserView(BaseView):
  @expose('/')
  def index(self):
    return self.render('users.html')

admin.add_view(UserView(name=u'Hello'))

app.run()