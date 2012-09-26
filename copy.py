#!/usr/bin/env python
import shutil

def copyAllChangedFiles():
    f = open("changed_files", "r")
    for line in f:
        filename = line.strip("\n").strip("\r")
        dest = "/Users/jeffyu/applications/postgresql-9.1.4/" + filename
        src="/Users/jeffyu/works/unsw/dbsampling/"+filename
        shutil.copyfile(src, dest)

if __name__ == "__main__":
   copyAllChangedFiles() 
   print "copied successfully"
