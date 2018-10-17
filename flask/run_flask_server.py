
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """<h1>Hello World!</h1>
    """

@app.route("/page")
def page():
    return "This is a page"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

if __name__ == "__main__":
    app.run()




