import tarfile
import glob


def create_tarfile():
    tfile = tarfile.open("mytarfileTxt.tar", "w")
    for configfile in glob.glob("/home/*.txt"): #glob find all py files
        tfile.add(configfile) 
    tfile.close()


create_tarfile()
