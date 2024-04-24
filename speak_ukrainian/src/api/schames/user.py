from marshmallow import fields

from speak_ukrainian.src.api.schames import BaseSchema


class UserResource:
    def __init__(self, id, email, firstName, lastName, password,  phone, roleName, status, urlLogo):
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.phone = phone
        self.roleName = roleName
        self.status = status
        self.urlLogo = urlLogo

    def __eq__(self, other):
        return (self.id == other.id
                and self.email == other.email
                and self.firstName == other.firstName
                and self.lastName == other.lastName
                and self.phone == other.phone
                and self.roleName == other.roleName
                and self.status == other.status
                and self.urlLogo == other.urlLogo)


class UserResponseSchema(BaseSchema):
    model_class = UserResource

    id = fields.Int()
    firstName = fields.Str()
    lastName = fields.Str()
    email = fields.Str()
    password = fields.Str()
    phone = fields.Str()
    roleName = fields.Str()
    urlLogo = fields.Str()
    status = fields.Str()
