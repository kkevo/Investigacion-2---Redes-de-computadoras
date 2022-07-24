#Servidor
from base64 import decode
import socket
host="LocalHost"
port=5656
server=socket.socket(socket.AF_INET, socket.IPPROTO_TCP)
server.bind((host,port))
server.listen(1)
print("Servidor en espera de conexion: ")
act_con, addr=server.accept()

while True:
    ack=act_con.recv(1024)
    ack_decode=ack.decode(encoding="ascii", errors="ignore")
    print("Cliente: ",ack_decode)
    send=ack_decode.upper()
    print("Se recibio bien el string y se paso a mayusculas")
    act_con.send(send.encode(encoding="ascii", errors="ignore"))
    