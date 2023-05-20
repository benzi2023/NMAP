import os
import ipaddress
from ping3 import ping

def get_devices_in_range(network_range):
    network = ipaddress.ip_network(network_range)
    devices = []
    
    for ip in network.hosts():
        ip = str(ip)
        response_time = ping(ip, timeout=1)
        if response_time is not None:
            devices.append(ip)
    
    return devices

if __name__ == "__main__":
    network_range = input("Ingresa el rango de red (ejemplo: 192.168.1.0/24): ")
    devices = get_devices_in_range(network_range)
    
    print("Dispositivos encendidos:")
    for device in devices:
        print(device)
    
    print("Total de dispositivos encendidos:", len(devices))
