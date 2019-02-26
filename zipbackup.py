import zipfile
import os

class zipbackup(object):

    def __init__(self, filename_, path_, archtype_):
        self.filename = filename_
        self.path = path_
        self.archtype = archtype_

    def __del__(self):
        print("Экземпляр класса уничтожен")

    def Bzipfile(self, filename, path):
        return "Файлы по пути " + path + " архивированы в архив " + filename

    def Bextract(self):
        result = ""
        try:
            wr = zipfile.ZipFile(self.filename, self.archtype)
            wr.extractall(self.path)
            result = "Архив " + self.filename + " распакован в каталог " + self.path
        except Exception as Ex:
            result = "Error: " + str(Ex)
        return result
