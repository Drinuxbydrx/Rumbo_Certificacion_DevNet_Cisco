import csv

class ExtractorDispositivos:
    def __init__(self,ruta_archivo_csv):
        self.__ruta_archivo_csv = ruta_archivo_csv
        self.__nombre_dispositivo="router"
    def extractordedispositivos(self):
        with open(self.__ruta_archivo_csv,mode="r",encoding="utf-8") as archivo_csv:
            lector = csv.reader(archivo_csv)
            for fila in lector:
                if self.__nombre_dispositivo in fila:
                    print(fila)
        archivo_csv.close()