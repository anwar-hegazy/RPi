# Echo client program for IPv6 and IPv4
import socket
import sys

HOST = '192.168.0.14'    # The remote host (RPi IP)
PORT = 55005             # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error, msg:
        s = None
        continue
    try:
        s.connect(sa)
    except socket.error, msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print 'could not open socket'
    sys.exit(1)
s.send('7778888')
data = s.recv(1024)
s.close()
print 'Received test number:', repr(data)

