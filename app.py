from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# enable CORS
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


from blueprints import ping_bp

# 注册蓝图
app.register_blueprint(ping_bp)

if __name__ == '__main__':
    app.run()
