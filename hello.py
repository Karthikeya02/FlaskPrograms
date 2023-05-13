from flask import Flask

app = Flask(__name__)

'''
ROUTES
TEMPLATES
FORMS
EXTENSIONS
'''
# Home Page
@app.route('/')
def hompage():
    return 'Welcome to the Home Page!'

# Hello Page
@app.route('/hello')
def hello():
    return 'Hello, World!'

# User Page
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hello, %s!' % username

# Unique URLs / Redirection Behavior


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()
