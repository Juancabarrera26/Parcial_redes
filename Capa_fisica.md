# **Capa Física - Redes de Computadoras**  

## ** Punto 1: Evaluación de la Capa Física y Transformada de Fourier**  

### **🔹 Contexto**  
En la **capa física** del modelo OSI, la transmisión de datos se hace a través de señales **analógicas y digitales** que viajan por distintos medios (cables, fibra óptica, ondas de radio, etc.). Para entender cómo estas señales se comportan y cómo se pueden ver afectadas por interferencias o pérdidas de datos, se utilizan herramientas matemáticas como la **Transformada de Fourier**. Esta transformada nos permite analizar las señales en el **dominio de la frecuencia**, lo que es clave para mejorar la transmisión y evitar problemas en la comunicación.  

---

### * Pregunta 1: ¿Cómo contribuye la Transformada de Fourier al análisis de señales en la capa física?**  

La **Transformada de Fourier** (TF) es súper importante en redes de comunicación porque nos ayuda a descomponer cualquier señal en sus **componentes de frecuencia**. En otras palabras, nos permite ver de qué frecuencias está compuesta una señal y cómo se comporta en el espectro de transmisión.  

#### ** Aplicaciones en redes de computadoras:**  
1. **Análisis del ancho de banda:**  
   - Nos permite saber si una señal ocupa más ancho de banda del que debería. Si una señal se sale del rango permitido, podría causar interferencias con otras señales.  
   - También ayuda a optimizar el uso del canal, asegurando que la transmisión sea eficiente.  

2. **Identificación de ruido e interferencias:**  
   - Al analizar la señal en el dominio de la frecuencia, podemos detectar **ruidos o distorsiones** que podrían afectar la transmisión.  
   - Por ejemplo, si hay picos inesperados en el espectro de frecuencia, podríamos estar recibiendo interferencias de otra fuente de transmisión.  

En resumen, la **Transformada de Fourier** permite visualizar cómo se comportan las señales en el canal de transmisión, ayudando a mejorar su calidad y evitando problemas de comunicación.  

---

### ** Pregunta 2: Señales compuestas y espectro de frecuencias**  

Si una señal transmitida está compuesta por **tres sinusoides de diferentes frecuencias** (\( f_1 \), \( f_2 \), \( f_3 \)), lo que tenemos es una **señal periódica** que puede descomponerse en estas tres frecuencias fundamentales.  

#### ** ¿Cómo se vería esta señal en el dominio de la frecuencia?**  
- Al aplicar la **Transformada de Fourier**, lo que obtenemos es un **espectro de frecuencias** donde aparecen **tres picos**, cada uno en las posiciones \( f_1 \), \( f_2 \) y \( f_3 \).  
- La altura de cada pico corresponde a la **amplitud** de cada una de las sinusoides que componen la señal.  
- Si hubiera más frecuencias en la señal, veríamos más picos en el espectro.  

#### ** ¿Por qué es útil este análisis?**  
- Nos ayuda a entender cómo se distribuyen las frecuencias en una señal y si encajan dentro del ancho de banda permitido en el canal de comunicación.  
- También permite detectar posibles interferencias o pérdidas de información si observamos que ciertas frecuencias han sido atenuadas.  

En conclusión, la Transformada de Fourier nos ayuda a analizar **cómo se comportan las señales en redes de computadoras**, optimizando la transmisión y evitando problemas de comunicación.  

---
