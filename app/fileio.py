import os
import pwd
import datetime
from config import ROOTDIR

def dirlist(path):
    abs_path = ROOTDIR + path
    dirs = [x for x in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path,x))]
    return dirs

def filelist(path):
    abs_path = ROOTDIR + path
    files = [x for x in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path,x))]
    return files

def stat(path):
    return os.stat(ROOTDIR + path)

def getstats(path, folder='', get_bytes=False):
    stats = stat(folder + '/' + path)
    result = {
        "name": path,
        "owner": pwd.getpwuid(stats.st_uid).pw_name,
        "modTime": datetime.datetime.fromtimestamp(stats.st_mtime),
    }
    if get_bytes:
        result['byteSize'] = stats.st_size
    return result
