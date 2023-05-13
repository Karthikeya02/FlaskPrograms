from flask import Flask

app = Flask(__name__)

'''
ROUTES
TEMPLATES
FORMS
EXTENSIONS
'''

@app.route('/')
def hompage():
    return 'Welcome to the Home Page!'


@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
