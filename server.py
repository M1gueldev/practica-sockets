import socket
# Libreria para poder leer la fecha del systema
from datetime import datetime


# Definimos el host en localhost y el puerto en 9876
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 9876

# Creamos el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Escuchando en el puerto %s ...' % SERVER_PORT)

while True:    
    # Esperamos por conecciones 
    client_connection, client_address = server_socket.accept()

    # Obtenemos la request y la imprimimos
    request = client_connection.recv(1024).decode()
    print(request)

    # Enviamos la fecha y hora como respuesta

    now = datetime.now()

    response = now.strftime("%d/%m/%Y %H:%M:%S")
    client_connection.sendall(response.encode())
    client_connection.close()

# Cerramos el socket
server_socket.close()
