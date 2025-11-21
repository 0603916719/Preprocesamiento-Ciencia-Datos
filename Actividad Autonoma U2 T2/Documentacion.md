Optimización de código para la búsqueda de números primos

Introducción
Para realizar la actividad autónoma, desarrolle el codigo que permita analizar el rendimiento del programa en Python que busca todos los números primos en el rango de 1 a 100.000. El código inicial utiliza una función es_primo(n) que verifica si un número es primo probando todos los divisores posibles desde 2 hasta n-1. Luego, recorre el rango completo con un bucle for y va agregando a una lista los números que resultan primos. Aunque el algoritmo es correcto desde el punto de vista lógico, presenta un problema importante de eficiencia: realiza demasiadas operaciones de división y repite comprobaciones innecesarias, especialmente para números grandes. Al medir el tiempo de ejecución, observé que el programa tarda en promedio alrededor de 52 segundos, lo cual es excesivo para un rango relativamente pequeño y evidencia la necesidad de aplicar técnicas de optimización tanto a nivel algorítmico como a nivel de implementación en Python.
Para alcanzar la optimización del programa fue necesario revisar bibliografía especializada que respalda las decisiones técnicas aplicadas. La documentación oficial de Python permitió comprender el funcionamiento de herramientas de análisis de rendimiento como cProfile, fundamentales para identificar las funciones más costosas. De igual manera, la guía oficial de NumPy proporcionó criterios para mejorar la eficiencia en el manejo de arreglos y operaciones numéricas, lo que contribuyó significativamente a acelerar el procesamiento.

Optimización
Como segundo paso para mejorar el rendimiento del programa apliqué tres estrategias principales. En primer lugar, optimicé la función de verificación de primos. En lugar de probar todos los divisores hasta n-1, limité las comprobaciones hasta la raíz cuadrada de n usando math.isqrt(n). Esto se basa en el hecho matemático de que, si un número no tiene divisores menores o iguales a su raíz cuadrada, ya no los va a tener en el resto del rango, lo que reduce drásticamente el número de iteraciones. En segundo lugar, reemplacé el bucle tradicional con append por una lista, lo que hace el código más compacto y, además, aprovecha mejor las optimizaciones internas de Python para la construcción de listas. Finalmente, incorporé la librería NumPy para generar el rango de números como un arreglo (np.arange(1, 100001)), lo que facilita el manejo del conjunto de datos y prepara el código para posibles extensiones vectorizadas. Estas tres mejoras combinadas permiten reducir el número de operaciones y aprovechar estructuras más eficientes, tanto a nivel de CPU como de código Python.

Resultados
Para evaluar el impacto de las optimizaciones, medí los tiempos de ejecución de ambas versiones en tres repeticiones. Los resultados para el código original fueron aproximadamente: 48.34 s, 58.52 s y 49.27 s, dando un tiempo promedio cercano a 52.04 segundos. En cambio, el código optimizado obtuvo tiempos de 0.2136 s, 0.2223 s y 0.2034 s, con un promedio de alrededor de 0.21 segundos. Esto significa que la versión optimizada es aproximadamente 250 veces más rápida que la original al resolver exactamente el mismo problema y sobre el mismo rango de datos.

Conclusiones
La optimización del código para la búsqueda de números primos tuvo un efecto importante en el rendimiento global del programa. Al aplicar mejoras simples pero bien fundamentadas, como limitar el rango de divisores hasta la raíz cuadrada, utilizar list comprehensions y aprovechar estructuras de datos eficientes como los arreglos de NumPy se logró reducir el tiempo de ejecución de alrededor de 52 segundos a solo 0.21 segundos.
Como recomendación para futuros desarrollos, considero fundamental realizar siempre una primera medición de tiempos antes y después de cualquier cambio importante, apoyándose en herramientas como time y cProfile. También es conveniente analizar las funciones críticas que más tiempo consumen y replantear su diseño antes de pensar en soluciones más complejas. 

ANEXOS
1.	Código inicial
2.	Código de optimización
3.	Código para comparar los tiempos
4.	Histograma de valores en tiempos
 

Bibliografía
Python Software Foundation. (2024). Los perfiladores de Python: profile y cProfile. En Documentación de Python 3.13. Recuperado de la documentación oficial de Python. (Python documentation)
NumPy Developers. (2025). NumPy documentation: User guide and API reference. NumPy Project. Recuperado de la documentación oficial de NumPy. (numpy.org)
Ghidarcea, M. (2024). Prime number sieving—A systematic review with benchmarks. Algorithms, 17(4), 157. https://doi.org/10.3390/a17040157 (MDPI)

