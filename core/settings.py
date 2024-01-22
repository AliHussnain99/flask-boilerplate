from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from core.middlewares.maintenance import MaintenanceModeMiddleware

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)

# APP LEVEL CONFIGURATIONS
from core.utils.helpers import get_env_variable, get_db_url, initiate_logging

app.config['SECRET_KEY'] = get_env_variable('SECRET_KEY')
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = get_env_variable('SWAGGER_API_TITLE')
app.config['API_VERSION'] = get_env_variable('SWAGGER_API_VERSION')
app.config['OPENAPI_VERSION'] = get_env_variable('SWAGGER_OPENAPI_VERSION')
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = get_env_variable('SWAGGER_ENDPOINT')
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
migrate = Migrate(app, db)

# LOGGING CONFIGURATIONS ON THE BASIS OF ENV
initiate_logging(app)

# MIDDLEWARES
app.wsgi_app = MaintenanceModeMiddleware(app.wsgi_app, app, maintenance_mode=get_env_variable('MAINTENANCE_MODE'))

# IMPORTING MODELS AND VIEWS
from .models import *
from .views import *

from .utils.celery import celery
