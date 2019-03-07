from zipbackup import *
import sys

print("PyBackupper: 1.0.0.0e")
if len(sys.argv) > 3:
    if sys.argv[1] == "-a":
        zip = zipbackup(sys.argv[2], sys.argv[3], 'w')
        print(zip.Bzipfile())
        del zip
    elif sys.argv[1] == "-e":
        zip = zipbackup(sys.argv[2], sys.argv[3], 'r')
        print(zip.Bextract())
        del zip
