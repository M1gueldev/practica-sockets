# Informe practica de sockets

## Miguel Murillo Bernal

## 9117995 LP

# DNS Resolver

```{python}
import socket
import sys

# La libreria sys es para poder leer los datos de entrada del CLI como la url y la 
# asignamos en la varable a
a = sys.argv[1]
# La libreria socket tiene una funcion que nos permite saber la IP de una url asi que la
# interpolamos en un string de salida en STD
print(f"La dirección IP de {a} es {socket.gethostbyname(a)}")
```

# TCP Server

```{python}
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
```
# TCP CLiente

```{python}

import socket
# Libraria para leer argumentos del CLI
import sys

a = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((a, 80))

# Generamos el mensaje para enviar en formato bytes 
v = b"GET / HTTP/1.1\r\nHost:%b\r\n\r\n" % a.encode()

# Enviamos el mensaje
sock.send(v)
# Recibimos la respuesta
response = sock.recv(4096)
# Cerramos la coneccion
sock.close()
# Imprimimos la respuesta
print(response.decode())
```
