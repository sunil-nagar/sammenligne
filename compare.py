import os
import datetime
import mime_types


def modified(path):
    mtime = os.path.getmtime(path)
    mtime = datetime.fromtimestamp(mtime)
    mtime = mtime.strftime("%Y%m%d%H%M%S")


def size(path):
    return os.path.getsize(path)


def extension(path):
    name, extension = os.path.splitext(path)
    return extension
