import socket

localIP     = "LocalHost"
localPort   = 5656
bufferSize  = 1024

# Se crea el socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Se asocian la direccion y el puerto
UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP inicializado")

# El servidor espera la llegada de sockets
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print(f"Mensaje del cliente: {message}")

    message = message.decode(encoding="ascii", errors="ignore")
    message = message.upper()
    message = str.encode(message)

    # Enviar respuesta al cliente
    UDPServerSocket.sendto(message, address)