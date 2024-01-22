from flask.views import MethodView
from flask_smorest import Blueprint

from core.settings import db, app
from .models import User
from .schemas import UserSchema
from .tasks import task_long

blp = Blueprint("User", "__name__", description="This handles all user functionality")


@blp.route("/users")
class UserCreateListAPIView(MethodView):
    model = User

    @blp.response(200, UserSchema(many=True))
    def get(self):
        app.logger.debug("Retrieving data from the database")
        task_long.delay()
        return self.model.query.all()

    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema())
    def post(self, data):
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user
