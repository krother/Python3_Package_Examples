
# bottle

### What it is good for?

Create simple web applications.

Bottle is a minimalistic framework, yet it has all components for creating dynamic web pages: URLs, HTML templates, variables etc. For a web page like the authors blog it is more than sufficient.

### Installed with Python by default

no

### Installed with Anaconda

no, but the very similar framework `flask` is!

### Example

Start a web server on port 8080:

    from bottle import default_app, route, run, get, post, request

    @get('/form')
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


### Where to learn more?

[http://bottlepy.org](http://bottlepy.org)
