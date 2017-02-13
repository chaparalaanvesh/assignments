from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is home page'

@app.route('/anvi')
def anvi():
    return 'This is anvesh learning the Flask'

@app.route('/profile/<username>')
def profile(username):
    return 'hey there %s' % username

@app.route('/profile_id/<int:id')
def profile_id(id):
    return 'hey there %d' % id


if __name__ == '__main__':
    app.run(debug=True)
