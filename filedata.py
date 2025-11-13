import os
import filecmp
from datetime import datetime

from mime_types import is_binary
from log import debug


UNKNOWN = 0
TEXT = 1
CLASS = 2
ZIP = 3
_AR = 4  # jar, war, ear


class FileData:
    path = ""
    exists = False
    name = ""
    extension = ""
    modified = 0
    size = 0
    binary = True
    etype = UNKNOWN

    def __init__(self, path):
        self.path = path
        if path is None or len(path) == 0:
            return
        self.exists = os.path.exists(path)
        if self.exists:
            self.directory = os.path.dirname(path)
            self.name, self.extension = os.path.splitext(path)
            if not self.extension:
                self.extension = ""
            self.extension = self.extension.lower()
            modified = os.path.getmtime(path)
            modified = datetime.fromtimestamp(modified)
            self.modified = modified.strftime("%Y%m%d%H%M%S")
            self.size = os.path.getsize(path)
            self.binary = is_binary(path)
            if not self.binary:
                self.etype = TEXT
            if self.extension == ".zip":
                self.etype = ZIP
            if self.extension == ".class":
                self.etype = CLASS
            if self.extension == ".jar":
                self.etype = _AR
            if self.extension == ".war":
                self.etype = _AR
            if self.extension == ".ear":
                self.etype = _AR

    def print(self):
        print(
            self.path,
            self.exists,
            self.name,
            self.extension,
            self.modified,
            self.size,
            self.binary,
            self.etype,
        )
