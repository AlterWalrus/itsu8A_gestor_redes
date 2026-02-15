import nmap
import socket

def obtener_segmento():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()

        segmento = ".".join(ip_local.split(".")[:-1]) + ".0/24"
        return segmento
    except Exception:
        return "192.168.1.0/24"


def escanear_red(segmento):
    nm = nmap.PortScanner()
    nm.scan(hosts=segmento, arguments='-sn')
    
    dispositivos_encontrados = []
    
    for host in nm.all_hosts():
        ip = host
        nombre = nm[host].hostname() if nm[host].hostname() else "Desconocido"
        mac = nm[host]['addresses'].get('mac', '00:00:00:00:00:00')
        fabricante = nm[host]['vendor'].get(mac, 'Genérico')
        
        dispositivos_encontrados.append({
            'nombre': nombre,
            'ip': ip,
            'mac': mac,
            'fabricante': fabricante
        })
    
    return dispositivos_encontrados