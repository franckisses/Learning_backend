
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % (username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % (subpath)

# # ----------------------------------------------
# from flask import request

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return '注册'
#     else:
#         return '登陆'

# if __name__ == "__main__":
#     app.run()

from flask import Flask,redirect,url_for,request,jsonify,make_response
from werkzeug.routing import BaseConverter
# 创建Flask的应用对象
app = Flask(__name__, static_url_path='/python')    # __name__ 就是当前模块的名字

# 装饰器，绑定视图函数的路径
@app.route('/')
def hello_world():
    # 视图函数
    return 'Hello World!'


@app.route("/post_only", methods=["POST"])
def post_only():
    return "post"


# 装饰器不同 访问同一个视图函数
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi nihao"

# 重定向
@app.route("/login")
def login():
    url = '/'
    return redirect(url)

# 我们可以发现上面的url是写死的，
# 那如果某一天我把hello1视图函数的装饰器修改了，
# 那我岂不是还要一个一个去修改？所以这里还有另外一种方法：
@app.route("/login2")
def login2():
    url = url_for("hello_world")
    return redirect(url)

# 接受参数：

@app.route("/goods/<goods_id>")
def goods(goods_id):

    return "goods_id: %s" % goods_id
    
# @app.route("/goods/<int:goods_id>")
# def goods(goods_id):
#      return "goods_id: %s" % goods_id


# 1.定义自己的转换器
class RegexConverte(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverte, self).__init__(url_map)
        # 将正则表达式的参数保存在对象的属性中，flask会去使用这个属性来进行路由的正则匹配
        self.regex = regex

# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverte

@app.route("/send/<re(r'1[345678]\d{9}'):moblie>")
def send_sms(moblie):
    return "send_sms: %s" % moblie
app.debug = True
# 重写改方法
# class MobileConverte(BaseConverter):
#     def __init__(self,url_map):
#         # 调用父类的初始化方法
#         super(MobileConverte, self).__init__(url_map)
#         self.regex = r'1[345678]\d{9}'

# # 2. 将自定义的转换器添加到flask的应用中
# app.url_map.converters["mobile"] = MobileConverte

# @app.route("<mobile:moblie_num>")
# def send_sms(moblie_num):
#     return "send_sms: %s" % moblie_num

@app.route("/post", methods=["GET","POST"])
def post():
    if request.method == 'GET':
        print(request.args)
        name = request.args.get("name")
        age = request.args.get("age")
        print(name,age)
        return "hello name=%s age=%s" % (name, age)
    name = request.form.get("name")
    age = request.form.get("age")
    return "hello name=%s age=%s" % (name, age)

# 返回json数据。需要导入jsonify
@app.route("/index")
def index():
    data = {
        "name":"javaandpython",
        "age":20
    }
    return jsonify(data)

# 自定义返回的请求头。
@app.route("/index2")
def index2():
    resp = make_response("index page")
    resp.status = "666"
    resp.headers["city"] = "hn"
    return resp


# @app.route("/index")
# def index():
#     # 1. 通过元组来自定义返回响应信息
#     return ("index page", 400, {"itcast":"python","City":"hn"})

@app.errorhandler(404)
def handle_404_error(err):
    '''自定义的处理错误方法'''
    # 这个返回值会是用户在前端中所看到的结果
    return u"很抱歉，出现了404错误  错误信息: %s" % err
    
if __name__ == '__main__':
    # 运行本地服务器进行测试flask程序
    # app.run()
    # 通过url_map可以查看整个flask中的路由信息
    print(app.url_map)
    app.run(host="127.0.0.1", port="9000")
