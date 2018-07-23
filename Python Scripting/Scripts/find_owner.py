#!/usr/bin/python3


import os

uidset = set()

for line in open("/etc/passwd"):
    split = line.split(":")
    uidset.add(int(split[2]))

testdir = "/home/student"

for folder, dirs, files in os.walk(testdir):
    for file in files:
        path = folder + "/" + file
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            print(path + " not found")
            continue

        if attributes.st_uid not in uidset:
            print(path + " has no owner")

