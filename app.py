from flask import Flask, url_for, render_template, request, abort, redirect
from forms import show_the_login_form, do_the_login  # Import the functions


app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.get('/login-form')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    url_for('static', filename='style.css')