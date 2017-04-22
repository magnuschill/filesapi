import falcon
from app.fileio import filelist, getstats
from app.schemas.file import FileSchema

schema = FileSchema()

class FileResource(object):
    def on_get(self, req, resp, folder=''):
        resp.status = falcon.HTTP_200  # This is the default status
        results = [getstats(x, folder, get_bytes=True) for x in filelist(folder)]
        resp.body = schema.dumps(results, many=True).data
