# Comportamiento de TCP ante Congestión de Red

En redes de computadoras, el protocolo TCP (Transmission Control Protocol) es fundamental para garantizar la comunicación confiable entre dispositivos. Uno de sus mecanismos principales es el control de congestión, que ajusta dinámicamente la cantidad de datos que se pueden enviar sin recibir confirmación, esto con el fin de evitar que la red se sature. El método que se va a simular en este trabajo se basa en el comportamiento básico de TCP Tahoe, que consiste en un aumento progresivo de la ventana de congestión (cwnd) durante las transmisiones exitosas y un reinicio drástico al detectar pérdidas de paquetes.

## Objetivo
El propósito de este trabajo es implementar un script en Python que simule cómo se comporta la ventana de congestión de TCP (cwnd) bajo eventos de éxito o pérdida de paquetes, usando un sistema de probabilidades para determinar el éxito o falla de cada transmisión.

## Descripción del Código
El código está diseñado para simular 50 transmisiones consecutivas. Cada transmisión tiene una probabilidad del 80% de éxito y un 20% de fallo. Cuando se produce un éxito, la ventana de congestión aumenta en 1 (como en la fase de Slow Start). Cuando ocurre una pérdida, la ventana se restablece a 1.

### Código
```python
import random
import matplotlib.pyplot as plt

def simulate_tcp_congestion():
    cwnd = 1  # Tamaño inicial de la ventana 
    num_transmissions = 50  
    cwnd_values = []

    for i in range(1, num_transmissions + 1):
        if random.random() <= 0.8:  # Probabilidad de exito (80%)
            cwnd_values.append(cwnd)
            print(f"Transmision {i}: Exito - cwnd = {cwnd}")
            cwnd += 1  # Incremento en la ventana 
        else:  # Probabilidad de perdida (20%)
            cwnd_values.append(cwnd)
            print(f"Transmision {i}: Perdida - cwnd = 1")
            cwnd = 1  # Reinicio de la ventana 

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, num_transmissions + 1), cwnd_values, marker='o', linestyle='-', color='blue')
    plt.title('Comportamiento de TCP Tahoe ante Congestion de Red')
    plt.xlabel('Numero de Transmision')
    plt.ylabel('Tamaño de la Ventana de Congestion (cwnd)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_tcp_congestion()
```

### Explicación del Código
- **`simulate_tcp_congestion()`:** Esta función realiza la simulación de las transmisiones y ajusta la ventana de congestión (`cwnd`) según el resultado de cada transmisión.
- **`random.random()`:** Genera un número aleatorio entre 0 y 1. Si el número generado es menor o igual a 0.8, se considera un éxito; de lo contrario, se simula una pérdida.
- **Impresión de resultados:** Se muestran claramente los resultados de cada transmisión con el tamaño actual de la ventana de congestión.
- **`matplotlib.pyplot`:** Se utiliza para graficar el comportamiento de `cwnd` a lo largo de las transmisiones.


## Evidencias de Ejecución
El gráfico generado muestra cómo la ventana de congestión (`cwnd`) aumenta progresivamente durante transmisiones exitosas y se reinicia a 1 cuando ocurre una pérdida de paquete.

[![Captura-de-pantalla-2025-03-11-210325.png](https://i.postimg.cc/90dVgVvf/Captura-de-pantalla-2025-03-11-210325.png)](https://postimg.cc/QKdRHLNL)

[![Captura-de-pantalla-2025-03-11-210335.png](https://i.postimg.cc/6qJthTbS/Captura-de-pantalla-2025-03-11-210335.png)](https://postimg.cc/7GVFHPkM)

## Conclusión
Este script muestra de forma simplificada el comportamiento de TCP bajo condiciones de éxito y pérdida de paquetes. La simulación refleja adecuadamente el funcionamiento del control de congestión basado en TCP Tahoe. Además, la representación gráfica facilita la comprensión visual del comportamiento dinámico de la ventana de congestión.


