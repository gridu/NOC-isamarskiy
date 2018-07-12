#!/usr/bin/python3

import hashlib
import os


def gethash(file):
    hasher = hashlib.md5()
    with open(file, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()


hashmap = {}

for rootdir, dirs, files in os.walk("/home/student/"):
    for f in files:
        path = os.path.join(rootdir, f)

        if os.path.islink(path) or os.stat(path).st_size < 1024:
            continue
        try:
            hash = gethash(path)
            if hash in hashmap:
                matching = hashmap[hash]
                if os.stat(path).st_ino == os.stat(matching).st_ino:
                    print("%s, %s are links to same file" % (path, matching))
                    continue
                # Otherwise, delete the new file and link the name to the old one
                else:
                    os.unlink(path)
                    os.link(matching, path)
                    print("%s same as %s" % (path, matching))
            else:
                hashmap[hash] = path
        except PermissionError:
            print("need to be root")


