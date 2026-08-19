""" 
Se debe crear un archivo nombrado dispositivos.csv 
y que contenga la siguiente informacion 

hostname,ip,device_type
R1,192.168.1.1,router
SW1,192.168.1.2,switch
R2,192.168.1.3,router

El programa debe 
1.-Abrir el archivo utilizando open().
2.-Utilizar el módulo csv.
3.-Leer las líneas.
4.-Mostrar únicamente los dispositivos cuyo device_type sea "router"
5.-Cerrar el archivo utilizando close().
"""
from Class.ExtractorDispositivos import ExtractorDispositivos
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    ruta = BASE_DIR / "data" / "dispositivos.csv"
    extractor = ExtractorDispositivos(ruta)
    extractor.extractordedispositivos()