import socket

def iniciar_cliente(nombre_cliente):
    """Inicia el cliente y se conecta al servidor."""
    try:
        # Funcion para crear el socket del cliente
        sock_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_cliente.connect(("127.0.0.1", 2010))  
        print("Conectado al servidor en localhost:2010")

        # Funcion para enviar un mensaje al servidor
        mensaje = f"Hola, soy el cliente {nombre_cliente}"
        print(f"Enviando mensaje: {mensaje}")
        sock_cliente.send(mensaje.encode("utf-8"))

        # Funcion para recibir una respuesta del servidor
        respuesta = sock_cliente.recv(1024).decode("utf-8")
        print(f"Respuesta del servidor: {respuesta}")

    except Exception as e:
        print(f"Error en el cliente: {e}")

    finally:
        sock_cliente.close()

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    iniciar_cliente(nombre)
