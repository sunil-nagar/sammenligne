import os
import sys
import compare
import diffmsg
import utils
import fdiff
import zdiff
import mime_types

from log import trace, debug

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
            if compare.size(item1) != compare.size(item2):
                dm = diffmsg.create_size_mismatch(item1)
                dm.display()
                if not mime_types.is_binary(item1):
                    linediffs = fdiff.cdiff(item1, item2)
                    print(linediffs)
                if mime_types.is_zip(item1):
                    linediffs = zdiff.cdiff(item1, item2)
                    print(linediffs)


def deepdiff(dir1, dir2):
    diff(dir1, dir2)
    while len(queue) > 0:
        q = queue.pop()
        diff(q[0], q[1])


dir1 = sys.argv[1]
dir2 = sys.argv[2]
deepdiff(dir1, dir2)
