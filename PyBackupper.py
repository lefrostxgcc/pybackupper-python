from zipbackup import *

print("PyBackupper: 1.0.0.0b")
zip = zipbackup("backup2.zip", "/home/chip/python")
print(zip.Bzipfile(zip.filename, zip.path))
print(zip.Bextract(zip.filename, zip.path))
del zip
