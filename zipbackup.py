class zipbackup(object):

    def __init__(self, filename_, path_):
        self.filename = filename_
        self.path = path_

    def __del__(self):
        print("Экземпляр класса уничтожен")

    def Bzipfile(self, filename, path):
        return "Файлы по пути " + path + " архивированы в архив " + filename

    def Bextract(self, filename, path):
        return "Архив " + filename + " распакован в каталог " + path
