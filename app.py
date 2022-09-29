from flask import Flask

from blueprints import ping_bp


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 注册蓝图
app.register_blueprint(ping_bp)

if __name__ == '__main__':
    app.run()
