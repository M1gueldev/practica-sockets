import socket
import sys

# La libreria sys es para poder leer los datos de entrada del CLI como la url y la 
# asignamos en la varable a
a = sys.argv[1]
# La libreria socket tiene una funcion que nos permite saber la IP de una url asi que la
# interpolamos en un string de salida en STD
print(f"La dirección IP de {a} es {socket.gethostbyname(a)}")
