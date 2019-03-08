from zipbackup import *
import sys

print("PyBackupper: 1.0.0.0h")
try:
    if len(sys.argv) > 3:
        zip = zipbackup(sys.argv[2], sys.argv[3], sys.argv[1])
        print(zip.Bbackup())
        del zip
except FileNotFoundError:
    print("Файла " + sys.argv[2] + " не существует")
except Exception as ex:
    print('Error:', str(ex))
