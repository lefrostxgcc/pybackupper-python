import zipfile
import os

class zipbackup(object):

    def __init__(self, filename_, path_, command_):
        self.filename = filename_
        self.path = path_
        self.archtype = 'r'
        if command_ == '-a':
            self.archtype = 'w'
        elif command_ == '-e':
            self.archtype = 'r'
        elif command_ == '-v':
            self.archtype = 'r'
        self.command = command_

    def __del__(self):
        print("Экземпляр класса уничтожен")

    def Bbackup(self):
        result = ""
        try:
            wr = zipfile.ZipFile(self.filename, self.archtype)
            if self.command == '-a':
                result = self.addarchive(wr)
            elif self.command == '-e':
                result = self.extract(wr)
            elif self.command == '-v':
                result = self.view(wr)
            wr.close()
        except Exception as Ex:
            result = "Error: " + str(Ex)
        return result

    def addarchive(self, wr):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                wr.write(os.path.join(root, file))
        result = "Файлы по пути " + self.path + " архивированы в архив " + self.filename
        return result

    def extract(self, wr):
        wr.extractall(self.path)
        result = "Архив " + self.filename + " распакован в каталог " + self.path
        return result

    def view(self, wr):
        wr.printdir()
        result = ""
        return result
