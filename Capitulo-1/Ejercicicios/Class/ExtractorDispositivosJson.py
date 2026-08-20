import json

class ExtractorDispositivosJson:

    def __init__(self,ruta_archivo:str):
        self.__ruta_archivo = ruta_archivo
        self.__status_dispositivo = "down"
    def extractordedispositivosJSON(self):
        with open(self.__ruta_archivo,mode="r",encoding="UTF-8") as archivoJson :
            lector = json.load(archivoJson)
            archivoJson.close()
            for dispositivo in lector['devices']:
                        if self.__status_dispositivo in dispositivo['status']:
                            print(f"{dispositivo}")
            
            