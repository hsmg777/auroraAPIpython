from flask import Flask
from flask_smorest import Api
from resources.Fiestas import blp as FiestasBluePrint
from resources.About import blp as AboutBluePrint
from resources.Contact import blp as ContactBluePrint
from resources.Galeria import blp as GaleriaBluePrint
from resources.Politicas import blp as PoliticasBluePrint
from resources.Reservas import blp as ReservasBluePrint
from db import init_db, db
import urllib.parse  # Importar urllib.parse para manejar el string de conexión

def createApp():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "AuroraAPI"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    # Configuración de la base de datos
    server = '(localdb)\\MSSQLLocalDB'
    database = 'AuroraDataBase'
    username = 'aurora'
    password = 'mamifer1'
    driver = 'ODBC Driver 17 for SQL Server'

    # Crear el string de conexión con urllib.parse
    params = urllib.parse.quote_plus(
        f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la base de datos con la aplicación
    init_db(app)
    
    api = Api(app)
    #BLUEPRINTS ROUTES
    api.register_blueprint(FiestasBluePrint)
    api.register_blueprint(AboutBluePrint)
    api.register_blueprint(ContactBluePrint)
    api.register_blueprint(GaleriaBluePrint)
    api.register_blueprint(PoliticasBluePrint)
    api.register_blueprint(ReservasBluePrint)
    

    return app

if __name__ == '__main__':
    app = createApp()
    app.run(debug=True)
