

class ObjetoaJson:

    def __init__(self):
        self.__dispositivos = [
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
    @property   
    def getdispositivos(self):
        return self.__dispositivos