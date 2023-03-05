import socket
from binascii import hexlify

this_ip = socket.gethostbyname(socket.gethostname())

def convert_ip4_address():
  for ip_addr in ['127.0.0.1', '192.168.0.1', this_ip]:
    packed_ip_addr = socket.inet_aton(ip_addr)
    unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
    print("Ip Address : %s => Packed : %s, Unpacked : %s" 
          %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

if __name__ == "__main__":
  convert_ip4_address() 
