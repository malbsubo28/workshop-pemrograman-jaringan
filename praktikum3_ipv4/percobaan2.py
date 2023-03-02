import socket

def get_remote_machine_info():
  remote_host = 'www.python.org'
  try:
    print("IP Address of %s: %s" %(remote_host,
          socket.gethostbyname(remote_host)))
  except socket.error as err_meg:
    print("%s: %s" %(remote_host, err_meg))

if __name__ == "__main__":
    get_remote_machine_info()
