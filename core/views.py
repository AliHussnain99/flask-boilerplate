# REGISTER BLUEPRINTS
from core.settings import api
from user.views import blp as user_blp
api.register_blueprint(user_blp)
