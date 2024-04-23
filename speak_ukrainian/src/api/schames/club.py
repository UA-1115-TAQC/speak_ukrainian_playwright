from marshmallow import fields

from speak_ukrainian.src.api.schames import BaseSchema
from speak_ukrainian.src.api.schames.category import CategoryResponseSchema
from speak_ukrainian.src.api.schames.contacts import ContactDataResponseSchema


class ClubResponse:
    def __init__(self, id, ageFrom, ageTo, name, description,
                 urlWeb, urlLogo, urlBackground, urlGallery, workTimes,
                 categories, user, center, rating, locations,
                 isApproved, isOnline, feedbackCount, contacts):
        self.id = id
        self.ageFrom = ageFrom
        self.ageTo = ageTo
        self.name = name
        self.description = description
        self.categories = categories
        self.contacts = contacts
        self.urlWeb = urlWeb
        self.urlLogo = urlLogo
        self.urlBackground = urlBackground
        self.urlGallery = urlGallery
        self.workTimes = workTimes
        self.user = user
        self.center = center
        self.rating = rating
        self.locations = locations
        self.isApproved = isApproved
        self.isOnline = isOnline
        self.feedbackCount = feedbackCount


class ClubResponseSchema(BaseSchema):
    model_class = ClubResponse

    id = fields.Int()
    ageFrom = fields.Int()
    ageTo = fields.Int()
    name = fields.Str()
    description = fields.Str()
    categories = fields.List(
        fields.Nested(CategoryResponseSchema))
    contacts = fields.List(
        fields.Nested(ContactDataResponseSchema))
    urlWeb = fields.Str(allow_none=True)
    urlLogo = fields.Str()
    urlBackground = fields.Str(allow_none=True)
    urlGallery = fields.List(fields.Raw())
    workTimes = fields.List(fields.Raw())
    user = fields.Raw()
    center = fields.Raw(allow_none=True)
    isApproved = fields.Boolean(allow_none=True)
    isOnline = fields.Boolean()
    feedbackCount = fields.Int()
    rating = fields.Number()
    locations = fields.List(fields.Raw())
