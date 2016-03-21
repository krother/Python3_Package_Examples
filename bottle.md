
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

    from bottle import default_app, route, run

    @route('/')
    def index():
        characters = ['Hamlet', 'Ophelia', 'Polonius', 'Claudius']
        cast = "<h3>dramatis personae:</h3>"
        for char in characters:
            cast += '<li><a href="/{0}">{0}</a></li>'.format(char)
        return '<ul>{}</ul>'.format(cast)

    @route('/<char>')
    def enter_char(char):
        html = '''<h1>Enter {}</h1>
        <a href="/">back</a>'''.format(char)
        return html

    application = default_app()
    run(application, host='localhost', port=8080, reloader=True)


### Where to learn more?

[http://bottlepy.org](http://bottlepy.org)
