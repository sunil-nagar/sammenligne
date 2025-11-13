import zipfile

from log import info, warn
from datetime import datetime

def diff(zip1, zip2):
    data = []
    with zipfile.ZipFile(zip1) as z1, zipfile.ZipFile(zip2) as z2:
        names1, names2 = set(z1.namelist()), set(z2.namelist())
        missing1 = names2 - names1
        missing2 = names1 - names2
        if len(missing1) > 0:
            data.append("+++ " + zip1)
        if len(missing2) > 0:
            data.append("--- " + zip2)
        for missing in missing1:
            data.append(f"+ {missing}")
        for missing in missing2:
            data.append(f"- {missing}")
    return data


def cdiff(zip1, zip2):
    clean = diff(zip1, zip2)
    return "\n".join(clean)
