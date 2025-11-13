import subprocess
import re
from utils import line_matching, diff_list


def jar_manifest(f):
    # unzip -p /Users/nagars/Dev/jldapsearch/target/jldapsearch-1.0-SNAPSHOT.jar META-INF/MANIFEST.MF
    result = subprocess.run(["unzip", "-p", f, "META-INF/MANIFEST.MF"], 
                            capture_output=True, text=True, check=True)
    return result.stdout


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
    lines1 = structure(class1).splitlines()
    lines2 = structure(class2).splitlines()
    diff = diff_list(class1, class2, lines1, lines2)
    return diff


def cdiff(zip1, zip2):
    clean = diff(zip1, zip2)
    return "\n".join(clean)

def jdiff(jar1, jar2):
    lines1 = jar_manifest(jar1).splitlines()
    lines2 = jar_manifest(jar2).splitlines()
    diff = diff_list(jar1, jar2, lines1, lines2)
    return "\n".join(diff)
