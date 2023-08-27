import socket
import termcolor

# Function to scan a range of ports on a target
def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target, port)

# Function to scan a specific port on a target
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        # Port is closed or an error occurred
        #print("[-] Port Closed " + str(port))
        pass

# Get target input from the user
target = input("[*] Enter Target To Scan(Split Them By Comma (,)): ")

# Get the number of ports to scan from the user
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

# Check if multiple targets are provided
if ',' in target:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    # Split multiple targets and scan each one
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    # Scan a single target
    scan(target, ports)
