from flask import Flask

def create_app():
    # Inicializa a aplicação Flask
    app = Flask(__name__)

    # Registra as rotas
    from .routes import main
    app.register_blueprint(main)

    return app
