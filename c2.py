# -*- encoding=UTF-8 -*-
import requests
from flask import Flask, render_template, request, make_response, redirect, flash, get_flashed_messages
import  logging
from logging.handlers import  RotatingFileHandler

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '#'
app.secret_key = 'nowcoder'

'''
    入口的写法， 路径的映射
'''

@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for msg , category in get_flashed_messages(with_categories=True):
        res = res + category + msg  + '<br>'
    res += 'hello'
    return res


# 注意int:uid中间是没有空格的
# 注意/profile/<int:uid>/的最后一个斜杠
@app.route('/profile/<int:uid>/',methods=['GET','post' ])
def profile(uid):
    colors = ('red', 'green')
    infos = {'h' : 'hello', 'w' : 'world'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)

@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '[][][][]' + request.path + '<br>'
    for property in dir(request):
        res = res  + str(property) + '|==|<br>' + str(eval('request.' + property)) + '<br>'
    response = make_response(res)
    response.set_cookie('nowcodeid', key)
    response.status = '404'
    response.headers['babyJY'] = 'I LOVE~~'
    return response

    return res

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def direct_demo(code):
    return redirect('/newpath', code=code)

@app.errorhandler(400)
def exception_page(error):
    return 'exception'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url=request.url), 404


@app.route('/login')
def login():
    app.logger.info('log success')
    flash("登录成功", 'info')
    # return 'OK'
    return redirect('/')

@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'warn' : logging.WARN, 'error' : logging.ERROR, 'info' : logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level], msg)
    return  'logged: ' + msg


def set_logger():
    info_file_handler = RotatingFileHandler('G:\\NowProject\\NowcodeProject\\logs\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler = RotatingFileHandler('G:\\NowProject\\NowcodeProject\\logs\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler = RotatingFileHandler('G:\\NowProject\\NowcodeProject\\logs\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__ == '__main__':
    set_logger()
    app.run(debug=True)
    # profile.run(debug=True)
