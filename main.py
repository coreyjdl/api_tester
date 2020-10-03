from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/test')
def test():
    return 'Setup API response here.'