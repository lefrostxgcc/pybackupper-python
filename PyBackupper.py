from zipbackup import *

print("PyBackupper: 1.0.0.0b")
zip = zipbackup()
zip.filename = "backup1.zip"
zip.path = "/home/chip/python/"
print(zip.Bzipfile(zip.filename, zip.path))
print(zip.Bextract(zip.filename, zip.path))
