from marshmallow import fields

from speak_ukrainian.src.api.schames import BaseSchema


class ContactDataResponse:
    def __init__(self, contactType, contactData):
        self.contactType = contactType
        self.contactData = contactData

    def __eq__(self, other):
        return (self.contactType == other.contactType
                and self.contactData == other.contactData)


class ContactType:
    def __init__(self, id, name, urlLogo=''):
        self.id = id
        self.name = name
        self.urlLogo = urlLogo

    def __eq__(self, other):
        return (self.id == other.id
                and self.name == other.name)


class ContactTypeSchema(BaseSchema):
    model_class = ContactType

    id = fields.Int()
    name = fields.Str()
    urlLogo = fields.Str()


class ContactDataResponseSchema(BaseSchema):
    model_class = ContactDataResponse

    contactType = fields.Nested(ContactTypeSchema)
    contactData = fields.Str()
