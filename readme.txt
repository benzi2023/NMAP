# Programa para contar dispositivos encendidos en un rango de red

Este programa en Python te permite escanear un rango de red y contar los dispositivos que están encendidos dentro de ese rango.

## Requisitos

- Python 3.x instalado en tu sistema
- Biblioteca `ping3` instalada. Puedes instalarla usando el siguiente comando:

  ```shell
  pip install ping3
Uso
Ejecuta el programa utilizando el siguiente comando:
python programa.py
Se te pedirá que ingreses el rango de red que deseas escanear. Proporciona el rango de red en formato CIDR, por ejemplo: 192.168.1.0/24.

El programa enviará solicitudes de ping a todas las direcciones IP dentro del rango de red especificado y mostrará las direcciones IP de los dispositivos que respondan al ping.

Se mostrará una lista de dispositivos encendidos y el total de dispositivos encontrados.

Ingresa el rango de red (ejemplo: 192.168.1.0/24): 192.168.1.0/24

Dispositivos encendidos:
192.168.1.1
192.168.1.10
192.168.1.15

Total de dispositivos encendidos: 3

Eso es todo! Ahora puedes utilizar este programa para contar los dispositivos encendidos en tu rango de red. Si tienes alguna pregunta o problema, no dudes en contactarme.