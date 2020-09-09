from flask import Flask, request
import os

from flask.wrappers import Request

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='MY_SUPER_SECRET_KEY',
        DATABASE=os.path.join(app.instance_path, 'provider.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Put routes here:
    @app.route('/')
    def home():
        return {
            'status': 200,
            'message': "You are running the provider service!"
        }

    @app.route('/add')
    def adder():
        args = request.args
        x = args.get('x')
        y = args.get('y')
        sum = int(x) + int(y) 
        return {
            'sum': sum
        }

    return app
