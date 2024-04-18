from marshmallow import Schema, post_load


class BaseSchema(Schema):
    model_class = None
    @post_load
    def make_modal(self, data, **kwargs):
        return type(self).model_class(**data)