import nmap
import re

ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max= 65535

print(r"""
   |\---/|
   | ,_, |          Welcome to
    \_`_/-..----.
 ___/ `   ' ,""+ \  PYTHON PORT SCANNER 
(__...'   __\    |`.___.';
  (_,...'(_,.`__)/'.....+
""")


open_ports = []

while True:
    ip_add_input = input("\n Enter the ip to be scanned:- ")

    if ip_pattern.search(ip_add_input):
        print(f"{ip_add_input} is a valid ip address")
        break

while True:
    print("Enter the port range you want to scan in format: <int>-<int> (example would be 40-8080)")
    port_range = input("Enter port range: ")
    port_range_valid = port_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm=nmap.PortScanner()
for port in range(port_min,port_max +1):
    try:
        result = nm.scan(ip_add_input, str(port))
        port_status = (result['scan'][ip_add_input]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")

