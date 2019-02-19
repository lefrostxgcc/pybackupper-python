class zipbackup(object):
    filename = ""
    path = ""

    def Bzipfile(self, filename, path):
        return "Файлы по пути " + path + " архивированы в архив " + filename

    def Bextract(self, filename, path):
        return "Архив " + filename + " распакован в каталог " + path
