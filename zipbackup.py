import zipfile
import os

class zipbackup(object):

    def __init__(self, filename_, path_, archtype_):
        self.filename = filename_
        self.path = path_
        self.archtype = archtype_

    def __del__(self):
        print("Экземпляр класса уничтожен")

    def Bzipfile(self):
        result = ""
        try:
            wr = zipfile.ZipFile(self.filename, self.archtype)
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    wr.write(os.path.join(root, file))
                    result = "Файлы по пути " + self.path + " архивированы в архив " + self.filename
            wr.close()
        except Exception as Ex:
            result = "Error: " + str(Ex)
        return result

    def Bextract(self):
        result = ""
        try:
            wr = zipfile.ZipFile(self.filename, self.archtype)
            wr.extractall(self.path)
            result = "Архив " + self.filename + " распакован в каталог " + self.path
            wr.close()
        except Exception as Ex:
            result = "Error: " + str(Ex)
        return result
