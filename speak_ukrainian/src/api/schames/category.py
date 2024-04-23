from marshmallow import fields

from speak_ukrainian.src.api.schames import BaseSchema


class CategoryResponse:
    def __init__(self, id, sortby, name, description, urlLogo,
                 backgroundColor, tagBackgroundColor, tagTextColor):
        self.id = id
        self.sortby = sortby
        self.name = name
        self.description = description
        self.urlLogo = urlLogo
        self.backgroundColor = backgroundColor
        self.tagBackgroundColor = tagBackgroundColor
        self.tagTextColor = tagTextColor


class CategoryResponseSchema(BaseSchema):
    model_class = CategoryResponse

    id = fields.Int()
    sortby = fields.Int()
    name = fields.Str()
    description = fields.Str()
    urlLogo = fields.Str()
    backgroundColor = fields.Str()
    tagBackgroundColor = fields.Str()
    tagTextColor = fields.Str()
