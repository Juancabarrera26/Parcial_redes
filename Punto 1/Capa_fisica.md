# Capa Física en Redes de Computadoras

En la capa física del modelo OSI se lleva a cabo la transmisión de datos a través de medios como cables de cobre, fibra óptica y ondas de radio. Esta capa se encarga de enviar bits de forma directa, sin interpretación, lo que implica procesos como la modulación y la codificación. Es fundamental comprender el comportamiento de las señales, ya que estas pueden sufrir degradaciones (por ejemplo, por atenuación o interferencias) que afectan la calidad de la comunicación.

Una de las herramientas matemáticas que resulta indispensable en este análisis es la *Transformada de Fourier*, la cual permite descomponer una señal en sus componentes de frecuencia.

---

## Pregunta 1: ¿Cómo contribuye la Transformada de Fourier al análisis de señales en la capa física?

La Transformada de Fourier convierte una señal en función del tiempo, x(t), en su representación en el dominio de la frecuencia, X(f). Esto se expresa matemáticamente como:

[![Whats-App-Image-2025-03-12-at-12-59-26-PM.jpg](https://i.postimg.cc/NMk0mbNS/Whats-App-Image-2025-03-12-at-12-59-26-PM.jpg)](https://postimg.cc/bDd8j0f9)

Donde:
- *X(f)* representa la distribución de amplitudes según la frecuencia.
- *x(t)* es la señal original.
- *f* indica la frecuencia.
- *j* es la unidad imaginaria.

Esta transformación es muy útil porque, al pasar al dominio de la frecuencia, se puede:
- *Visualizar y analizar la distribución de energía:* Identificar las frecuencias predominantes en la señal.
- *Detectar interferencias y ruidos:* Un pico anómalo en el espectro puede indicar la presencia de un ruido que afecta la transmisión.
- *Optimizar el uso del ancho de banda:* Conociendo la asignación de frecuencias, se pueden diseñar sistemas que maximicen la eficiencia del canal.

Por ejemplo, en un canal con ancho de banda limitado de B Hz, conocer el espectro permite ajustar la señal para utilizar ese recurso de manera óptima.

---

## Pregunta 2: Señales compuestas y espectro de frecuencias

Considera una señal que es la suma de tres sinusoides de diferente frecuencia. Esta señal se puede expresar como:

[![Whats-App-Image-2025-03-12-at-12-59-31-PM.jpg](https://i.postimg.cc/FzPsnzXx/Whats-App-Image-2025-03-12-at-12-59-31-PM.jpg)](https://postimg.cc/rRrkD8md)

Donde:
- *A₁, A₂ y A₃* son las amplitudes de cada componente.
- *f₁, f₂ y f₃* son las frecuencias respectivas.

En el dominio del tiempo, la señal es la superposición de tres ondas, lo que genera una forma compleja. Sin embargo, al aplicar la Transformada de Fourier se obtiene una representación en el dominio de la frecuencia:

[![Whats-App-Image-2025-03-12-at-12-59-31-PM.jpg](https://i.postimg.cc/FzPsnzXx/Whats-App-Image-2025-03-12-at-12-59-31-PM.jpg)](https://postimg.cc/rRrkD8md)

En esta expresión, la función *δ(f − fᵢ)* (función delta de Dirac) se manifiesta como un pico en la frecuencia *fᵢ* con una amplitud proporcional a *Aᵢ. Esto significa que en el espectro se observarán tres picos claramente definidos, correspondientes a las frecuencias **f₁, f₂ y f₃*.

Esta representación es muy valiosa, ya que permite identificar de forma precisa los componentes que conforman la señal y detectar cualquier anomalía o interferencia que se encuentre fuera del rango esperado.

---

Este README puede visualizarse directamente en GitHub, mostrando las fórmulas renderizadas como imágenes. Si prefieres utilizar otro servicio (por ejemplo, CodeCogs o QuickLaTeX) o descargar las imágenes para subirlas de forma local, puedes ajustar los enlaces según tus necesidades.
