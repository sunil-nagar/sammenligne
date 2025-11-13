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



def is_binary(ext):
    if ext is None:
        return True
    if ext in BINARY:
        return True
    if ext in ZIP:
        return True
    if ext in TEXT:
        return False
    return True

