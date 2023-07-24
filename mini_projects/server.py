from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    return {'Hello, World!': 0}

if __name__ == '__main__':
    app.run()