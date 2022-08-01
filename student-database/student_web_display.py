from main import register, update, search
from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def main():
    return 'This is the main environment'

@app.route('/register')
def reg():
    return register()

@app.route('/search')
def sear():
    return search()

@app.route('/update')
def upd():
    return update()
app.run()