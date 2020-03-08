from flask import Flask
from flask import request
from flask import render_template
from time import gmtime, strftime

import mem_info, cpu_load, net_stat

app = Flask(__name__)

@app.route('/')
def home():
    str_t = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    return 'Welcome to HP Microserver, ' + str_t

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# this is for pebble
@app.route('/data/')
def data():
    return '''{"content":"''' + '''{0} \\n\\n Memory\\n {1} \\n\\n Network \\n {2}", "refresh":10, "theme":1, "updown":1 '''.format(cpu_load.load_stat(), mem_info.meminfo(), net_stat.netstat()) + '''}'''

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8888)
