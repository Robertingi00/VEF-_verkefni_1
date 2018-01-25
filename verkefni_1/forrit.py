from bottle import *
import os

@route('/')
def index():
    return "<a href='/about'>About</a>" \
           "<a href='/biography'> Biography</a>" \
           "<a href='/pictures'> Pictures</a>"




@route('/about')
def about():
    return "You are in about"

@route('/biography')
def biography():
    return "You are in biography"

@route('/pictures')
def pictures():
    return "You are in pictueres"



run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
