# coding=utf-8
from flask import Blueprint, render_template, abort, request, session

common = Blueprint('common', __name__, template_folder='templates')

@common.route('/')
@common.route('/index')
def index():
  user_info = session["loged_user"]
  return render_template('index.html', user = user_info)