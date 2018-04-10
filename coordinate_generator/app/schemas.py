import re
from marshmallow import Schema, fields, validates, ValidationError


class CoordinateRequestSchema(Schema):
    func = fields.Str(required=True)
    start = fields.DateTime(required=True)
    end = fields.DateTime(required=True)
    dt = fields.Int(required=True)

    @validates('func')
    def validate_quantity(self, value):
        if value.find("t") == -1:
            raise ValidationError('Bad function')

        if re.match("^(?!.*?[a-su-zA-Z\=]).*$", value) is None:
            raise ValidationError('Bad function')
