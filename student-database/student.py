from re import A
from register import register
from search import search
from update import update
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
