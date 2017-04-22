import falcon
from app.resources.file import FileResource
from app.resources.folder import FolderResource

application = falcon.API()

files = FileResource()
folders = FolderResource()

application.add_route('/folders/', folders)
application.add_route('/files/', files)
application.add_route('/{folder}/files/', files)


