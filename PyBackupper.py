from zipbackup import *

print("PyBackupper: 1.0.0.0b")
zip = zipbackup("/home/chip/python/test/zip/backup_2.zip", "/home/chip/python", "r")
#print(zip.Bzipfile(zip.filename, zip.path))
print(zip.Bextract())
del zip
