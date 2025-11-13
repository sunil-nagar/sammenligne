import os
import sys
import compare
import diffmsg
import utils
import fdiff
import zdiff
import jdiff
import mime_types
import argparse

from log import trace, debug

parser = argparse.ArgumentParser(
    prog="sammenligne",
    description="Directory difference tool",
    epilog="Beware all ye who enter here!",
)

parser.add_argument('dir1') # positional argument
parser.add_argument('dir2') # positional argument
parser.add_argument('-e', '--extension', default='')
parser.add_argument('-n', '--namecontains', default='')
parser.add_argument('-t', '--trimlines', default=120)
parser.add_argument('-d', '--displaylines', default=120)
parser.add_argument('-c', '--classfiles', action='store_true')

args = parser.parse_args()
print(f"Comparing {args.dir1} to {args.dir2}")
print(f"Options: -e {args.extension} -n {args.namecontains} -t {args.trimlines} -d {args.displaylines}")


queue = []


def diff(dir1, dir2):
    trace("Diffing", dir1, dir2, "...")
    paths = utils.list_all(dir1, dir2)
    for path in paths:
        item1 = dir1 + path
        item2 = dir2 + path
        trace("Comparing", item1, item2, "...")
        if not os.path.exists(item1):
            dm = diffmsg.create_not_found(item1)
            dm.display()
        elif not os.path.exists(item2):
            dm = diffmsg.create_not_found(item2)
            dm.display()
        elif os.path.isdir(item1):
            queue.append([item1, item2])
        else:
            if not args.namecontains in item1:
                continue
            size1 = compare.size(item1)
            size2 = compare.size(item2)
            if size1 != size2:
                dm = diffmsg.create_size_mismatch(item1, size1, size2)
                dm.display()
                if not mime_types.is_extension(item1, args.extension):
                    continue
                if not mime_types.is_binary(item1):
                    linediffs = fdiff.cdiff(item1, item2, 
                                            args.trimlines, args.displaylines)
                    print(linediffs)
                if mime_types.is_zip(item1):
                    linediffs = zdiff.cdiff(item1, item2)
                    print(linediffs)
                if args.classfiles:
                    if mime_types.is_extension(item1, "class"):
                        majver1 = jdiff.major_version(item1)
                        majver2 = jdiff.major_version(item2)
                        if majver1 != majver2:
                            dm = diffmsg.create_major_version_mismatch(item1, majver1, majver2)
                            dm.display()
                        linediffs = jdiff.cdiff(item1, item2)
                        print(linediffs)



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
