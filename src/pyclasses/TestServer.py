# Created by labattula on 02/07/16.


import socket

s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host, port))
s.listen(5)

while true:
  c, addr = s.accept()
  print ('Got the connection from', addr)
  c.send('thank you for the connection')
  c.close()