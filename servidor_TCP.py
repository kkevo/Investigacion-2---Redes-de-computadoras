#Servidor TCP
from base64 import decode
#Se importa la libreria socket utilizada para definir los protocolos y enviar el mensaje
import socket
#Se define el host 
host="LocalHost"
#Se define el puerto al cual se enviara respuesta
port=5656
#Se define el socket con sus respectivos protocolos, en este caso IPv4(AF_INET) y TCP(IPPROTO_TCP)
server=socket.socket(socket.AF_INET, socket.IPPROTO_TCP)
#Se define la direccion y el puerto al socket
server.bind((host,port))
#Se le dice al socket del servidor que escuche al cliente para poder recibir mensajes
server.listen(1)
#Se imprime que el servidor esta activo  y en espera
print("Servidor en espera de conexion: ")
#Se acepta el mensaje del cliente 
act_con, addr=server.accept()

# Se forma un loop infinito para la conexion entre servidor y cliente
while True:
    #Se crea una  variable que recibe el mensaje del cliente
    ack=act_con.recv(1024)
    #Se decodifica el mensaje del cliente en ascii
    ack_decode=ack.decode(encoding="ascii", errors="ignore")
    #Se imprime en pantalla el mensaje del cliente
    print("Cliente: ",ack_decode)
    #Se pasa el mensaje del cliente a mayusculas 
    send=ack_decode.upper()
    #Se imprime que se realizo bien el cambio a mayusculas
    print("Se recibio bien el string y se paso a mayusculas")
    #Se envia la respuesta del servidor al cliente codificada de forma ascii
    act_con.send(send.encode(encoding="ascii", errors="ignore"))
    
    