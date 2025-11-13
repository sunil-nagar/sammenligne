import subprocess
import re
from utils import line_begins, diff_list


def jar_manifest(f):
    result = subprocess.run(
        ["unzip", "-p", f, "META-INF/MANIFEST.MF"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def jdiff(jar1, jar2):
    lines1 = jar_manifest(jar1).splitlines()
    lines2 = jar_manifest(jar2).splitlines()
    diff = diff_list(jar1, jar2, lines1, lines2)
    return "\n".join(diff)


def structure_verbose(f):
    result = subprocess.run(
        ["javap", "-verbose", f], capture_output=True, text=True, check=True
    )
    lines = line_begins(result.stdout, ["major version", "public"])
    return lines


def diff(class1, class2):
    lines1 = structure_verbose(class1)
    lines2 = structure_verbose(class2)
    diff = diff_list(class1, class2, lines1, lines2)
    return diff


def cdiff(zip1, zip2):
    clean = diff(zip1, zip2)
    return "\n".join(clean)
