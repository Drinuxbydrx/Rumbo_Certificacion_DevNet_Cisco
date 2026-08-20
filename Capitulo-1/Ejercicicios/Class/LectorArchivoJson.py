import json

class LectorArchivoJson:

    def __init__(self,ruta_archivo):
        self.__ruta_archivo = ruta_archivo
    def lector(self):

        with open(self.__ruta_archivo,mode="r",encoding="UTF-8") as archivo:
            datos = json.load(archivo)
            print(datos)
