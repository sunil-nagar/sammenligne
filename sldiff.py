import os
import diffmsg
import utils
import fdiff
import zdiff
import jdiff
import argparse

from filedata import FileData
import filedata

from log import trace, debug

parser = argparse.ArgumentParser(
    prog="sammenligne",
    description="Directory difference tool",
    epilog="Beware all ye who enter here!",
)

parser.add_argument("dir1")  # positional argument
parser.add_argument("dir2")  # positional argument
parser.add_argument("-e", "--extension", default="")
parser.add_argument("-n", "--namecontains", default="")
parser.add_argument("-t", "--trimlines", default=120)
parser.add_argument("-d", "--displaylines", default=120)
parser.add_argument("-c", "--classfiles", action="store_true")

args = parser.parse_args()
print(f"Comparing {args.dir1} to {args.dir2}")
print(
    f"Options: -e {args.extension} -n {args.namecontains} -t {args.trimlines} -d {args.displaylines} -c {args.classfiles}"
)


queue = []

def printne(str):
    if str is None: return
    if len(str.strip()) == 0: return
    print(str)

def diff(dir1, dir2):
    trace("Diffing", dir1, dir2, "...")
    paths = utils.list_all(dir1, dir2)
    for path in paths:
        item1 = dir1 + path
        item2 = dir2 + path
        trace("Comparing", item1, item2, "...")
        fd1 = FileData(item1)
        fd2 = FileData(item2)
        if not fd1.exists:
            dm = diffmsg.create_not_found(item1)
            dm.display()
        elif not fd2.exists:
            dm = diffmsg.create_not_found(item2)
            dm.display()
        elif os.path.isdir(item1):
            queue.append([item1, item2])
        else:
            if not args.namecontains in item1:
                continue
            if not args.extension in fd1.extension:
                continue
            if fd1.size != fd2.size:
                dm = diffmsg.create_size_mismatch(item1, fd1.size, fd2.size)
                dm.display()
            if fd1.etype == filedata.TEXT:
                linediffs = fdiff.cdiff(item1, item2, args.trimlines, args.displaylines)
                printne(linediffs)
            if fd1.etype == filedata.ZIP:
                linediffs = zdiff.cdiff(item1, item2)
                printne(linediffs)
            if fd1.etype == filedata._AR:
                linediffs = jdiff.jdiff(item1, item2)
                printne(linediffs)
                linediffs = zdiff.cdiff(item1, item2)
                printne(linediffs)
            if args.classfiles:
                if fd1.etype == filedata.CLASS:
                    classdiffs = jdiff.cdiff(item1, item2)
                    printne(classdiffs)


def deepdiff(dir1, dir2):
    diff(dir1, dir2)
    while len(queue) > 0:
        q = queue.pop()
        diff(q[0], q[1])


if not os.path.exists(args.dir1):
    print(f"{args.dir1} not found...")
elif not os.path.exists(args.dir2):
    print(f"{args.dir2} not found...")
else:
    deepdiff(args.dir1, args.dir2)
