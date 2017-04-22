import falcon
from app.fileio import dirlist, getstats
from app.schemas.folder import FolderSchema

schema = FolderSchema()

class FolderResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status
        results = [getstats(x) for x in dirlist('')]
        resp.body = schema.dumps(results, many=True).data
