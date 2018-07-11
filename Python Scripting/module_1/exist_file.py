#!/usr/bin/python3

import os.path

exist_path="/etc/hosts"
none_exist_path="/etc/blabla"

if os.path.exists(exist_path):
    print("hosts file exists")
else:
    print("no hosts file")

if os.path.exists(none_exist_path):
    print("hosts file exists")
else:
    print("no hosts file")

