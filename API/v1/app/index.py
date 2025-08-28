import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# Carga las variables del .env
load_dotenv()

mongo = PyMongo()

def create_app():
    # Definir la carpeta de templates y static
    app = Flask(
        __name__,
        template_folder="templates",  # index.html va aquí
        static_folder="static"       # app.js y demás archivos estáticos
    )

    # Usa la variable del entorno en lugar de hardcodear la URI
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    mongo.init_app(app)

    CORS(app, origins="*")

    # Registro de Blueprints
    from .controladores.prendas import prendas_endpoints
    app.register_blueprint(prendas_endpoints, url_prefix="/admin2/api/v1")

    from .controladores.usuarios import usuarios_endpoints
    app.register_blueprint(usuarios_endpoints, url_prefix="/admin2/api/v1")

    from .controladores.ventas import ventas_endpoints
    app.register_blueprint(ventas_endpoints, url_prefix="/admin2/api/v1")

    from .controladores.reportes import reportes_endpoints
    app.register_blueprint(reportes_endpoints, url_prefix="/admin2/api/v1")

    # Ruta principal para mostrar la página web
    @app.route("/")
    def index():
        return render_template("index.html")

    return app
