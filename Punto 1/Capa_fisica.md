# Capa Física en Redes de Computadoras

En la capa física del modelo OSI se lleva a cabo la transmisión de datos a través de medios como cables de cobre, fibra óptica y ondas de radio. Esta capa se encarga de enviar bits de forma directa, sin interpretación, lo que implica procesos como la modulación y la codificación. Es fundamental comprender el comportamiento de las señales, ya que estas pueden sufrir degradaciones (por ejemplo, por atenuación o interferencias) que afectan la calidad de la comunicación.

Una de las herramientas matemáticas que resulta indispensable en este análisis es la Transformada de Fourier, la cual permite descomponer una señal en sus componentes de frecuencia.

⸻

# Pregunta 1: ¿Cómo contribuye la Transformada de Fourier al análisis de señales en la capa física?

La Transformada de Fourier convierte una señal en función del tiempo, x(t), en su representación en el dominio de la frecuencia, X(f). Esto se expresa matemáticamente como:

(https://chart.googleapis.com/chart?cht=tx&chl=X(f)%20%3D%20%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D%20x(t)%20e%5E%7B-j%202%5Cpi%20f%20t%7D%20dt)

Donde:
	•	X(f) representa la distribución de amplitudes según la frecuencia.
	•	x(t) es la señal original.
	•	f indica la frecuencia.
	•	j es la unidad imaginaria.

Esta transformación resulta muy útil porque, al pasar al dominio de la frecuencia, es posible:
	•	Visualizar y analizar la distribución de energía: Se identifica cuáles son las frecuencias predominantes en la señal.
	•	Detectar interferencias y ruidos: Por ejemplo, un pico anómalo en el espectro puede indicar la presencia de un ruido que afecta la transmisión.
	•	Optimizar el uso del ancho de banda: Conociendo la asignación de frecuencias, se pueden diseñar sistemas que maximicen la eficiencia del canal.

En términos prácticos, si se dispone de un canal con un ancho de banda limitado de B Hz, conocer el espectro permite ajustar la señal para que se utilice de manera óptima ese recurso.

⸻

# Pregunta 2: Señales compuestas y espectro de frecuencias

Consideremos una señal que resulta de la suma de tres sinusoides de diferente frecuencia. Esta señal se puede expresar como:

x(t) = A_1 \sin(2\pi f_1 t) + A_2 \sin(2\pi f_2 t) + A_3 \sin(2\pi f_3 t)

Aquí:
	•	A_1, A_2 y A_3 son las amplitudes de cada componente.
	•	f_1, f_2 y f_3 son las frecuencias correspondientes.

En el dominio del tiempo, la señal es la suma de tres ondas que se superponen, lo que genera una forma compleja. Sin embargo, al aplicar la Transformada de Fourier, se obtiene una representación en el dominio de la frecuencia:

X(f) = A_1\, \delta(f - f_1) + A_2\, \delta(f - f_2) + A_3\, \delta(f - f_3)

En esta expresión, \delta(f - f_i) es la función delta de Dirac, que se manifiesta como un pico en la frecuencia f_i con una amplitud proporcional a A_i. Esto significa que en el espectro de frecuencias se observarán tres picos claramente definidos, correspondientes a las frecuencias f_1, f_2 y f_3.

Esta representación es muy valiosa, pues permite identificar de forma precisa los componentes que conforman la señal y detectar cualquier anomalía o interferencia que se encuentre fuera del rango esperado.
