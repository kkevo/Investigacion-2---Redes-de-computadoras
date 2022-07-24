import socket

serverAddressPort   = ("LocalHost", 5656)
bufferSize          = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviar al servidor usando el socket UDP
while True:
    message = input("Cliente:\n")
    bytesToSend = str.encode(message)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)    
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    print(f"Mensaje del servidor: {msgFromServer[0]}")
