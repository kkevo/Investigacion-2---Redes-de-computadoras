#Realizacion del cliente UDP

#Se importa la libreria socket, la cual es utilizada para definir los protocolos y enviar los mensajes
import socket

from numpy import concatenate
#Se define el host y el puerto a utilizar, en este caso el puerto es 5656 (primeros 1024 reservados) y el host es LocalHost(127.0.0.1)
serverAddressPort   = ("LocalHost", 5656)
# Se define el tamaño del buffer en bytes
bufferSize          = 1024

# Se determina el socket de UDP, para esto se le define el protocolo IPv4(AF_INET) y el tipo de protocolo el cual en este caso es UDP(SOCK_DGRAM)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#Se define un limite de conexiones cliente/servidor
connection_limit = 5

# Se genera un loop inifinito de conexion con el servidor
while True:
    #Se introduce el mensaje de parte del usuario que quiere enviar el cliente
    message = input("Cliente:\n")    
    #Se codifica el mensaje del usuario 
    bytesToSend = str.encode(message)
    #Se codifica para enviar mensaje a servidor(direccion y puerto)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    #Se codifica la recepcion de parte del servidor     
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
    #Se imprime el mensaje del servidor
    print(f"Mensaje del servidor: {msgFromServer[0]}\n")
    #Se verifica si el cliente solicita terminar el envio de caracteres
    #o si se alcanzo el limite
    if message == "fin" or connection_limit == 1:
        break
    print('eee', message)
    # Se le resta 1 al contador del limite de conexiones
    connection_limit -= 1