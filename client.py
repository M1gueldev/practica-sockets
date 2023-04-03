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
