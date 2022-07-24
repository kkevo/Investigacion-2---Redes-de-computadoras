#Cliente
#Se importa un modulo denominado socket la cual soporta conexiones de red IP
import socket
#Se debe definir un host(de donde se lanza el mensaje)
host="LocalHost" #LocalHost es la direccion que tenemos actualmente
#Se debe definir un puerto, los primeros 1024 puertos están reservados para comunicaciones directas.
port=5656
#Se crea el objeto del socket, el que se enviara y con cual protocolo
#AF_INET es protocolo IPv4
sock_obj=socket.socket(socket.AF_INET, socket.IPPROTO_TCP)
# Se conecta el objeto del socket entre el host y el puerto
sock_obj.connect((host,port))
print("Se inicia cliente")
#Se hace un loop para realizar la interacción
while True:
    send=input("Cliente: ")
    #Se codifica la palabra cliente debido a que va en aascii
    sock_obj.send(send.encode(encoding="ascii", errors="ignore"))
    ack=sock_obj.recv(1024)
    print(" Servidor: ", ack.decode(encoding="ascii", errors="ignore"))
    





