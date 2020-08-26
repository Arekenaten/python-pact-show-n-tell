from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='MY_SUPER_SECRET_KEY',
    )

    # Put routes here:
    @app.route('/')
    def home():
        return {
            'status': 200,
            'message': "You are running the consumer service!"
        }

    return app
