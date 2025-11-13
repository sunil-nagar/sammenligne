import re

from log import trace, debug

ZIP = [
    ".zip",
    ".jar",
    ".war",
    ".ear",
]

BINARY = [
    ".class",
    ".DS_Store",
    ".gif",
    ".jpg",
    ".png",
    ".svg",
    ".tif",
]
TEXT = [
    ".txt",
    ".java",
    ".xml",
    ".bat",
    ".sh",
    ".py",
    ".css",
    ".csv",
    ".html",
    ".gitignore",
    ".md",
    ".jsp",
    ".js",
    ".jspf",
    ".sql",
    ".wsdl",
    ".xhtml",
    ".xsl",
]


def extension(f):
    match = re.search(r"(\.[A-z0-9]+)$", f)
    if match is None:
        return None
    extension = match.group(0)
    trace("extension", extension)
    return extension

def is_extension(f, e):
    ext = extension(f)
    return e in ext

def is_base(f):
    trace("testing", f)
    if not f:
        return True
    if not "." in f:
        return True
    return True


def is_binary(f):
    value = is_base(f)
    ext = extension(f)
    if ext is None:
        return True
    if ext in BINARY:
        return True
    if ext in ZIP:
        return True
    if ext in TEXT:
        return False
    return True


def is_zip(f):
    ext = extension(f)
    if ext is None:
        return False
    if ext in ZIP:
        return True
    return False
