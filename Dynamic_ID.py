from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!  This is an app.py file contains just this text.'

@app.route('/second')
def second():
    return "second page"

@app.route('/third/<string:id>')
def third(id):
    return f"ID of this page is {id}"

if __name__=='__main__':
   app.run(debug=True)