import os


def relative_path(dir, path):
    return path.replace(dir, "")


def list_relative(dir):
    list = []
    with os.scandir(dir) as scan:
        for entry in scan:
            local_path = relative_path(dir, entry.path)
            list.append(local_path)
    return list


def list_all(dir1, dir2):
    all = list_relative(dir1)
    second = list_relative(dir2)
    for s in second:
        if s not in all:
            all.append(s)
    return all
