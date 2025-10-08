import sys
import socket
import time

usage="python port_scan.py TARGET START_PORT END_PORT"

print("-"*70)
print("python port scanner")
print("-"*70)
 

if(len(sys.argv) !=4):
    print(usage)
    sys.exit()

try:
    target=socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port=int(sys.argv[2])
end_port=int(sys.argv[3])
print("scaning target",target)


for port in range(start_port,end_port+1):

    print("scanning port:",port) 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    conn=s.connect_ex((target,port))
    if(not conn):
        print("port{} is open".format(port))

    s.close()
