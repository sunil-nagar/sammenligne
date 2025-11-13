import subprocess
import re
from utils import line_matching, diff_list


def major_version(f):
    result = subprocess.run(
        ["javap", "-verbose", f], capture_output=True, text=True, check=True
    )
    # {f} | grep 'major version' | cut -d':' -f2 | tr -d ' ' ")
    major_version = line_matching(result.stdout, "major version: ")
    # major_version = re.search(r'\d+', major_version).group()
    major_version = major_version.split(" ")[4]
    major_version = int(major_version)
    return major_version


def structure(f):
    result = subprocess.run(["javap", f], capture_output=True, text=True, check=True)
    return result.stdout


def diff(class1, class2):
    f1_major_version = major_version(class1)
    f2_major_version = major_version(class2)
    lines1 = structure(class1).splitlines()
    lines2 = structure(class2).splitlines()
    diff = diff_list(class1, class2, lines1, lines2)
    # print(f"{f1} {f1_major_version}")
    # print(f"{f2} {f2_major_version}")
    # print(diff)
    return diff


def cdiff(zip1, zip2):
    clean = diff(zip1, zip2)
    return "\n".join(clean)
