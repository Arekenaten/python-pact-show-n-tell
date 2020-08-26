from flask import Flask
import os

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

    return app
