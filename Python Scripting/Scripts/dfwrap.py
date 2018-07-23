#!/usr/bin/env python3
import subprocess

threshold = 80    # (%)
partition = "/"  

proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
for line in proc.stdout:
    splitline = line.decode().split()
    print(splitline[1] + " and " + splitline[5])
    if splitline[5] == partition:
        print("partition " + partition + " is " + splitline[4][:-1])
        if int(splitline[4][:-1]) > threshold:
            print("WARNING!")
            

   
