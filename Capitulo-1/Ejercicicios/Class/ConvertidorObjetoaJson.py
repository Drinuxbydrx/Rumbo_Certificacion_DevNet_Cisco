from .ObjetoaJson import ObjetoaJson
import json
class ConvertidorObjetoaJson:
    def __init__(self,objeto:ObjetoaJson):
        self.__objetoaconvertir = objeto
    def convertidor(self,ruta_archivo:str):
        with open(ruta_archivo,mode="w",encoding="UTF-8") as archivo :

           json.dump(self.__objetoaconvertir,archivo)
            
