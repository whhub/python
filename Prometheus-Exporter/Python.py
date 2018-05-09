from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/metrics/', methods=['GET'])
def alert():
    return '''abc{tag1="t1", tag2="t2"} 5.7
            def{tag3="t3", tag4="t4"} 6.8
    '''

if __name__ == '__main__':
    app.run(
        port=9114
    )
