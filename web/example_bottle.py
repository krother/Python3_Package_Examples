
# Start a web server on port 8080:

from bottle import default_app, route, run, get, post, request

@get('/')
def index():
    return '''
    <form action="/form" method="post">
        Word: <input name="word" type="text" />
        <input value="Send" type="submit" />
    </form>
    '''

@post('/form')
def eval_form():
    word = request.forms.get('word')
    html = '''<h1>You entered a word with {} characters</h1>
    <a href="/word/{}">show the word</a>
    '''.format(len(word), word)
    return html

@route('/word/<word>')
def show_word(word):
    html = '''<h1>The word is: {}</h1>
    <a href="/">back</a>'''.format(word)
    return html


application = default_app()
run(application, host='localhost', port=8080, reloader=True)
