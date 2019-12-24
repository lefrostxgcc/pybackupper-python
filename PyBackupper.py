from zipbackup import *
import sys
import json

print("PyBackupper: 1.0.0.0i")
try:
    if sys.argv[1] == 'af':
        f = open('b.json')
        data = json.load(f)
        print(data["arch"])
    elif len(sys.argv) > 3:
        zip = zipbackup(sys.argv[2], sys.argv[3], sys.argv[1])
        print(zip.Bbackup())
        del zip
except FileNotFoundError:
    print("Файла " + sys.argv[2] + " не существует")
except Exception as ex:
    print('Error:', str(ex))
