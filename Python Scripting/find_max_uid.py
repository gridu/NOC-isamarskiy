maxuid = 0
maxname=""
for line in open("/etc/passwd"):
    split = line.split(":")
    if int(split[2]) > maxuid:
           maxuid = int(split[2])
           maxname = split[0]

print(maxuid)
print(maxname)

