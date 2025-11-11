TRACE = 0
DEBUG = 1
INFO = 2
WARN = 3
ERROR = 4

level = DEBUG


def trace(*args):
    if level <= TRACE:
        log(*args)


def debug(*args):
    if level <= DEBUG:
        log(*args)


def info(*args):
    if level <= INFO:
        log(*args)


def warn(*args):
    if level <= WARN:
        log(*args)


def error(*args):
    if level <= ERROR:
        log(*args)


def log(*args):
    args = list(map(lambda x: "None" if x is None else x, args))
    args = list(map(lambda x: str(x) if not isinstance(x, str) else x, args))
    print(" ".join(args))
