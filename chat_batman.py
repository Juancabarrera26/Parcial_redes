import socket
import threading

PORT = 5005  # Puerto común para todos
BUFFER_SIZE = 1024

# IP BATMAN del nodo local
local_ip = input("Tu IP BATMAN (ej. 10.0.0.1): ")

# Crear socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((local_ip, PORT))

def listen():
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        print(f"Mensaje de {addr[0]}: {data.decode()}\n> ", end="")

# Hilo para recibir mensajes
thread = threading.Thread(target=listen, daemon=True)
thread.start()

# Enviar mensajes
print("Chat BATMAN iniciado. Escribe 'salir' para terminar.")
while True:
    dest_ip = input("> IP destino: ")
    message = input("> Mensaje: ")
    if message.lower() == "salir":
        break
    sock.sendto(message.encode(), (dest_ip, PORT))