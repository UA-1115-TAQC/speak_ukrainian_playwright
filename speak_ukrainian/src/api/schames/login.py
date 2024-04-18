from marshmallow import fields

from speak_ukrainian.src.api.schames import BaseSchema


class SingInResponse:
    def __init__(self, id, email, roleName, accessToken, refreshToken):
        self.id = id
        self.email = email
        self.role_name = roleName
        self.access_token = accessToken
        self.refresh_token = refreshToken


class SignInResponseSchema(BaseSchema):
    model_class = SingInResponse

    id = fields.Int()
    email = fields.Str()
    roleName = fields.Str()
    accessToken = fields.Str()
    refreshToken = fields.Str()
