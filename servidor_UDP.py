#Servidor UDP
import socket

#Se define la direccion de IP o host a utilizar, en este caso es LocalHost (127.0.0.1)
localIP     = "LocalHost"
#Se define un puerto 
localPort   = 5656
#Se define el tamaño en bytes del mensaje 
bufferSize  = 1024

# Se crea el socket UDP con su respectivo protocolo IPv4 y protocolo UDP(SOCK_DGRAM)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Se asocian la direccion y el puerto 
UDPServerSocket.bind((localIP, localPort))

#Se define un limite de conexiones cliente/servidor
connection_limit = 5

print("Servidor UDP inicializado")
# El servidor espera la llegada de sockets
while(connection_limit>0):
    #Se reibe el mensaje en bytes del cliente
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    #Se define el mensaje y la direccion en sus respectivas posiciones
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    #Se imprime el mensaje que se recibio del cliente
    print(f"Mensaje del cliente: {message}\n")
    

    #Se decodifica el mensaje en ascii 
    message = message.decode(encoding="ascii", errors="ignore")
    # El mensaje del cliente se pasa a mayúscula 
    message = message.upper()
    #Se codifica el mensaje para ser enviado de vuelta
    message_encoded = str.encode(message)

    #Se envia la resouesta al cliente con el mensaje y su respectiva direccion
    UDPServerSocket.sendto(message_encoded, address)   

    # Se verifica si el cliente solicita terminar el envio de caracteres
    if str(message) == 'FIN':
        connection_limit = 0     

    #Se verifica si se alcanzo el limite
    if  connection_limit == 1:
        break

    # Se le resta 1 al contador del limite de conexiones
    connection_limit -= 1