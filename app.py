from flask import Flask, Request
from flask_script import Manager
from goods import goods

manage = Manager()
app = Flask(__name__)
app.register_blueprint(goods, url_prefix="/goods")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manage.run()
