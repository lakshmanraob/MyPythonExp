# Created by labattula on 13/01/16.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

if __name__ == 'main':
    app.run(debug=True)