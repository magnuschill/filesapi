from marshmallow import Schema, fields

class FolderSchema(Schema):
    name = fields.String()
    owner = fields.String()
    modTime = fields.DateTime()
