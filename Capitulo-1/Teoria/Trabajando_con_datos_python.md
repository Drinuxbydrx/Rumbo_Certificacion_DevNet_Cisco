## Parseo de Datos

El parseo de datos consiste en interpretar datos estructurados y convertirlos a una representacion que el programa pueda entender.

Ejemplo se recibe una estructua de datos de esta forma

```ini
drinux,35,pentester
ana,33,periodista
eluid,40,corredor
```
Cual quier programador viendo la estructura rapidamente puede decir la primer columna correspone al nikname y la segunda columna correspone a la edad y asi sucesivamente y a qui es donde entra nuestra definicion de parseo de datos ya que podemos lograr a traves del parseo una estructura como la siguiente:

```ini
{
  "nombre":"drinux",
  "edad":"35",
  "especialidad":"pentester"
}
```

Dentro de la automatizacion podemos encontrarnos con datos que viajan a traves de la diferente comunicacion entre sistemas.

Esta comunicacion puede llevarse a cabo a traves de 

* APIs
* routers
* switches
* servidores
* bases de datos

entre muchos sistemas mas cada sistema puede enviar diferente informacion utilizando diferentes formatos como :

* CSV
* JSON
* XML
* YAML

### CSV - Comma-Separated Values

CSV significa Valores separados por comas es uno de los formatos mas simples que existe para enviar o recibir datos crudos.
CSV sirve principalmente para representar datos tabulares en otras palabras informacion con estructura de una tabla.

```ini
IP,hostname,port
192.168.1.10,server01,22
192.168.1.20,server02,80
```

### CSV en Python

En el lenguaje python existe un modulo llamado **csv** el cual podemos importar de la siguiente manera

```python
import csv

archivo = open("servidores.csv")
lector= csv.reader(archivo)

for fila in lector :
    print(fila)
archivo.close()
```

si se tiene una estructura de datos como la siguiente:

```ini
IP,hostname,port
192.168.1.10,server01,22
192.168.1.20,server02,80
```
a la hora de ejecutar el script se puede obtener un parseo en los datos como el siguiente:

```python
['IP', 'hostname', 'port']
['192.168.1.10', 'server01', '22']
['192.168.1.20', 'server02', '80']
```
### JSON

Json significa Javascript Object Notation y es ampliamente utilizado en el envio y recepcion de datos entre :

* APIs REST
* Automatizacion
* Servidores web 

Cuenta con una estructura como la siguiente:

```ini
{"hostname":"router",
"ip":"192.168.1.1",
"vendor":"Cisco"
}
```
como se puede observar la estructura de JSON es mucho mas completa que la de CSV

### JSON en python

El lenguaje python con tiene un modulo llamado json el cual podemos importar de la siguente forma

```python
import json
```
y al realizar la importacion existen cuatro operaciones basicas: 

* json.load()
* json.loads()
* json.dump()
* json.dumps()

### Json.load()

La operacion load() sirve para leer Json desde un archivo

```python
import json 
archivo = open("datos.json") 
datos = json.load(archivo) 
archivo.close() 
print(datos)
```
```ini
{
  "hostname":"router",
  "ip": "192.168.1.1"
}
```
### Json.loads()

loads() significa load string practicamente se traduce como *interpretar JSON que se encuentra en una cadena de texto*

A qui no se trabaja con un archivo se trabaja con texto
```python
import json 
texto = '{"hostname": "router", "ip": "192.168.1.1"}'
datos = json.loads(texto) 
print(datos["hostname"])
```
### Json.dump()

La operacion dump() nos sirve para poder convertir algun objeto que tengamos en python en un archivo json.

```python
import json
datos={"hostname": "router","ip": "192.168.1.1"}
archivo = open("datos.json", "w")
json.dump(datos, archivo)
archivo.close()
```
### Json.dumps()

A qui en esta operacon nos ayuda a convertir un objeto python en una cadena JSON.

```python
import json
datos = {"hostname": "router","ip": "192.168.1.1"}
texto_json = json.dumps(datos)
print(texto_json)
```
para obtener en consola

```bash
{"hostname": "router", "ip": "192.168.1.1"}
```
### Ejemplo de parseo con Json

supongamos que recibimos una respuesta de la siguiente forma 

```bash
{"device":{"hostname":"R1","interfaces":["GigabitEthernet0/0","GigabitEthernet0/1"]}}
```

al escribir el codigo con la operacion **json.loads()** se interpreta y ya podemos accecder a la diferente informacion

```bash
 datos["device"]["hostname"]
 R1

 datos["device"]["interfaces"]
 ["GigabitEthernet0/0","GigabitEthernet0/1"]
```

### XML

XML significa Lenguaje de Marcado Extensible y su funcion principalmente xml representa informacion mediante etiquetas:

```ini
<device>
    <hostname>router-01</hostname>
    <ip>192.168.1.1</ip>
</device>
```
Y los datos XML se parsean de la siguiente forma:

```python

import xml.etree.ElementTree as ET

xml_data = """
<tienda>
    <producto id="101" categoria="electronica">
        <nombre>Laptop</nombre>
        <precio>1200</precio>
    </producto>
    <producto id="102" categoria="accesorios">
        <nombre>Mouse Wireless</nombre>
        <precio>25</precio>
    </producto>
</tienda>
"""
root = ET.fromstring(xml_data)
print(f"Etiqueta raiz: {root.tag}")

for producto in root.findall('producto'):
    prod_id = producto.get('id')
    categoria = producto.get('categoria')
    nombre = producto.find('nombre').text
    precio = producto.find('precio').text
    print(f"ID: {prod_id} | Producto: {nombre} | Precio: ${precio} | Cat: {categoria}")
```

* find('etiqueta'): Busca y devuelve unicamente la primera coincidencia que encuentra.
* findall('etiqueta'): Devuelve una lista con todas las coincidencias del mismo nivel.
* .text: Accede al valor de texto dentro del elemento.
* .get('atributo'): Devuelve el valor del atributo dentro de la etiqueta inicial (ejemplo: <producto id="101"> -> .get('id') regresa "101").

tambien xml se puede parsear con el modulo nativo de python **xmltodict**

```python
import xmltodict
data = xmltodict.parse(xml_data)
productos = data['tienda']['producto']
for prod in productos:
    print(f"{prod['nombre']}: ${prod['precio']} (ID: {prod['@id']})")
```

### YAML

Los archivos YML son una estructura de JSON estricto ya que todo documento JSON valido es tambien un YAML valido.

se puede instalar de la siguiente forma

```python
pip install pyyaml
```
Parseo de la estructura YAML

```python
import yaml
yaml_recibido = """
app:
  nombre: ScannerService
  version: 2.1
  puertos:
    - 80
    - 443
  base_datos:
    host: localhost
    puerto: 5432
"""
config = yaml.safe_load(yaml_recibido)
print(type(config))  # <class 'dict'>
print(f"Servicio: {config['app']['nombre']} en puerto {config['app']['base_datos']['puerto']}")
```
```python
import yaml
multi_documento = """
servidor: web
puerto: 80
---
servidor: db
puerto: 5432
"""
documentos = yaml.safe_load_all(multi_documento)
for doc in documentos:
    print(f"Servidor: {doc['servidor']} -> Puerto: {doc['puerto']}")
```

Envio de la estructura YAML

```python
import yaml
payload = {
    "target": "192.168.1.1",
    "scans": ["nmap", "gobuster"],
    "options": {"threads": 10, "verbose": True}
}
yaml_output = yaml.safe_dump(payload, default_flow_style=False, sort_keys=False)
print(yaml_output)
```
Constructores Personalizados
```python
import yaml
def env_var_constructor(loader, node):
    value = loader.construct_scalar(node)
    return f"RESOLVED_ENV[{value}]"
yaml.SafeLoader.add_constructor('!env', env_var_constructor)
yaml_custom = """
database_url: !env DB_PASSWORD
"""
data = yaml.safe_load(yaml_custom)
print(data['database_url'])
```