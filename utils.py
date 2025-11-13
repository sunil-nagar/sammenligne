import os


def line_matching(s, m):
    for line in s.splitlines():
        if m in line:
            return line
    return None

def diff_list(name1, name2, l1, l2):
    data = []
    s1, s2 = set(l1), set(l2)
    missing1 = s2 - s1
    missing2 = s1 - s2
    if len(missing1) > 0:
        data.append("+++ " + name1)
    if len(missing2) > 0:
        data.append("--- " + name2)
    for missing in missing1:
        data.append(f"+ {missing}")
    for missing in missing2:
        data.append(f"- {missing}")
    return data


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
