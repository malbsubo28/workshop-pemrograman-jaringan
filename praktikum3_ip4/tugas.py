import socket

def mencari_service_name():
  port = int(input("\nMasukkan port protokol : "))
  try:
    servicename = socket.getservbyport(port)
    print("Port : %s => service name : %s\n"
          %(port, servicename))
  except socket.error as error:
    print("Error : %s\n" %(error))

def mencari_alamat_ip():
  alamat_web = input("\nMasukkan alamat web : ")
  try:
    ip_addr = socket.gethostbyname(alamat_web)
    hostname = socket.getfqdn(alamat_web)
    ip_addr_serv = socket.gethostbyname(hostname)
    print("Anda mengakses %s dengan alamat IP %s"
          %(alamat_web, ip_addr))
    print("dari komputer %s dengan alamat IP %s\n"
          %(hostname, ip_addr_serv))
  except socket.error as error:
    print("Error : %s\n" %(error))

def reinput():
  ans = input("Anda ingin mengulang (y/t) ? ")
  if ans == "y": opt_input()
  elif ans != "t": print("Masukkan piliha 'y' atau 't' !"); reinput()

def opt_input():
  print("1. Mencari Service dan Protokol Pada Jaringan")
  print("2. Mencari Alamat Ip dari Sebuah Website")
  opt = input("Masukkan pilihan (1/2) ? ")
  if opt == "1": mencari_service_name(); reinput()
  elif opt == "2": mencari_alamat_ip(); reinput()
  else: print("\nMasukkan pilihan 1 atau 2 !"); opt_input()

opt_input()
