"""
dispositivos = [
    {
        "hostname": "R1",
        "ip": "192.168.1.1",
        "type": "router"
    },
    {
        "hostname": "SW1",
        "ip": "192.168.1.2",
        "type": "switch"
    }
]
1.-Creamos el objeto python
2.-Abrir un archivo llamado: reporte.json
3.-Utilizar:json.dump()
4.-Guardar la estructura dentro del archivo.
5.-Cerrar el archivo con close().
6.-Volver a abrir reporte.json.
7.-Utilizar json.load().
8.-Mostrar los dispositivos que acaba de recuperar.
"""

from Class.ObjetoaJson import ObjetoaJson
from Class.ConvertidorObjetoaJson import ConvertidorObjetoaJson
from Class.LectorArchivoJson import LectorArchivoJson
from pathlib import Path

if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent
    ruta = BASE_DIR / "data" / "reporte.json"

    objeto = ObjetoaJson()
    objetopython = objeto.getdispositivos
    convertidor = ConvertidorObjetoaJson(objetopython)
    convertidor.convertidor(ruta)
    lector = LectorArchivoJson(ruta)
    lector.lector()