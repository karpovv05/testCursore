import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask работает!'

if __name__ == '__main__':
    app.run(debug=True)

