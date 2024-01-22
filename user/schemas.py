from core.settings import ma
from .models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
