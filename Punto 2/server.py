import socket
import threading

def manejar_cliente(sock_cliente, direccion_cliente):
    """Maneja la conexión con un cliente."""
    print(f"Conexión aceptada desde {direccion_cliente}")

    try:
        # Funcion para recibir mensaje del cliente
        mensaje = sock_cliente.recv(1024).decode("utf-8")
        print(f"Mensaje recibido: {mensaje}")

        # Funcion para extraer nombre del cliente del mensaje
        if "Hola, soy el cliente" in mensaje:
            nombre_cliente = mensaje.split("Hola, soy el cliente")[-1].strip()
        else:
            nombre_cliente = "Desconocido"

        # Funcion para responder al cliente
        respuesta = f"Mensaje recibido de {nombre_cliente}"
        sock_cliente.send(respuesta.encode("utf-8"))
        print(f"Respuesta enviada: {respuesta}")

    except Exception as e:
        print(f"Error con el cliente {direccion_cliente}: {e}")

    finally:
        sock_cliente.close()
        print(f"Conexión cerrada con {direccion_cliente}")

def iniciar_servidor():
    """Inicia el servidor en el puerto 2010 y acepta múltiples clientes."""
    sock_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_servidor.bind(("0.0.0.0", 2010))  
    sock_servidor.listen(5)  
    print("Servidor escuchando en el puerto 2010...")

    while True:
        sock_cliente, direccion_cliente = sock_servidor.accept()
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(sock_cliente, direccion_cliente))
        hilo_cliente.start()

if __name__ == "__main__":
    iniciar_servidor()
