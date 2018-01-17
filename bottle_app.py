from bottle import route, run

@route('/')
def index():
    return "<a href='/about'>About</a>" \
           "<a href='/biography'> Biography</a>" \
           "<a href='/pictures'> Pictures</a>"




@route('/about')
def bottle():
    return "You are in about"

@route('/biography')
def bottle():
    return "You are in biography"

@route('/pictures')
def bottle():
    return "You are in pictueres"


run()
