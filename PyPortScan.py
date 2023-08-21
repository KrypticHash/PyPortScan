import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        print("[-] Port Closed " + str(port))

target = input("[*] Enter Target To Scan(Split Them By Comma (,)): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in target:
    print("[*] Scanning Multiple Targets")
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(target, ports)
