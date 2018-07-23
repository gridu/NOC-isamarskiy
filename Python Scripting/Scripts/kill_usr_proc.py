#!/usr/bin/python3

#Программа Python для уничтожения всех процессов, принадлежащих указанному пользователю

import pwd
import glob
import os
import signal

def getprocessuid(procdir):
    statusfile = open(procdir + "/status")
    for line in statusfile:
        if line.startswith("Uid:"):
            splitline = line.split()
            uid = int(splitline[2])
            return uid

username = 'student'

try:
    pwdentry = pwd.getpwnam(username)
except KeyError:
    print("error: no such user!")
    exit(1)

targetuid = pwdentry.pw_uid

print("target uid is %d" % targetuid)

os.chdir("/proc")

procdirlist = glob.glob("[0-9]*")

for procdir in procdirlist:
    if getprocessuid(procdir) == targetuid:
        print("killing process %s" % procdir)
        os.kill(int(procdir), signal.SIGTERM)



