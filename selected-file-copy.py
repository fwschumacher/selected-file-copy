# selected-file-copy.py
#
# Copies files from one location to another. Files to be copied are specified
# in a text file thereby limiting what gets copied. Source and target directories
# are assumed to be different. Omitting the file list will cause the script
# to abort.
#
# Usage: python selected-file-copy.py <source dir> <target dir> <list of files>
#
# Revision History
# ----------------------------------
# 1.0 2018-09-05 FS Original version

import glob
import sys
import os
import shutil

def copyfiles():

    # exit prematurely if file list is not specified on the command line
    if filelist == "":
        print("Usage: python selected-file-copy.py <source> <target> <filelist>")
        sys.exit()

    # read the list of files to be copied
    l = list()
    fl = open(filelist)
    while True:
        n = fl.readline().rstrip('\n')
        if n != "":
            l.append(n)
        else:
            break
    fl.close()

    # copy files from source to target
    files = glob.glob(filesource + '\\*.*')
    for f in files:
        fn = os.path.basename(f)
        if fn in l:
            print('Copying ' + fn)
            shutil.copy(f, filetarget)
    
    print('Done')

if __name__ == '__main__':
    filesource = os.path.dirname(sys.path[0])
    filetarget = os.path.dirname(sys.path[0])
    filelist = ""
    if len(sys.argv) > 1:
        filesource = sys.argv[1]
        filetarget = sys.argv[2]
        filelist = sys.argv[3]
    copyfiles()

# eof