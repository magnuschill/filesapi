from marshmallow import Schema, fields

class FileSchema(Schema):
    name = fields.String()
    owner = fields.String()
    modTime = fields.DateTime()
    byteSize = fields.Integer()
