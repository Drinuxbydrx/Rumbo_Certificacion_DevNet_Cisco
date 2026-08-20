"""
Se debe crear un archivo nombrado devices.json

y dentro del archivo debe contener

{
    "devices": [
        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "type": "router",
            "status": "up"
        },
        {
            "hostname": "SW1",
            "ip": "192.168.1.2",
            "type": "switch",
            "status": "up"
        },
        {
            "hostname": "R2",
            "ip": "192.168.1.3",
            "type": "router",
            "status": "down"
        }
    ]
}
* abrir devices.json con open()
* utilizar json.load()
* cerrar el archivo con close()
* recorrer los dispositivos
* mostrar solamente los dispositivos cuyo status sea "down"
"""
from Class.ExtractorDispositivosJson import ExtractorDispositivosJson
from pathlib import Path

if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent
    ruta = BASE_DIR / "data" / "devices.json"

    extractor_status_down = ExtractorDispositivosJson(ruta)
    extractor_status_down.extractordedispositivosJSON()
