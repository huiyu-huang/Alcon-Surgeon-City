import flask
def create_app():
    app=Flask(__name__)
    from .testFunction import main
    app.register_blueprint(main)


    return app
