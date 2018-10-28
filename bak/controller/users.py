class UserView(BaseView):

#这里类似于app.route()，处理url请求

@expose('/')

def index(self):

return self.render('index.html')

admin.add_view(MyView(name=u'Hello'))