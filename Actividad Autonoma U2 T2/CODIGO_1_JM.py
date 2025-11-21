import time

# Función para verificar si un número es primo (versión sin optimizar)
def es_primo(n):
    # Los números menores a 2 no son primos
    if n < 2:
        return False
    
    # Recorro todos los números desde 2 hasta n-1
    for i in range(2, n):
        # Si encuentro un divisor exacto, no es primo
        if n % i == 0:
            return False
    
    # Si no tuvo divisores, es primo
    return True


# Inicio del conteo de tiempo
inicio = time.time()

primos = []  # Aquí voy a guardar todos los números primos

# Recorro todos los números desde 1 hasta 100000
for num in range(1, 100001):
    if es_primo(num):
        primos.append(num)

# Fin del conteo de tiempo
fin = time.time()

# Muestro cuántos primos encontré
print("Cantidad de números primos encontrados:", len(primos))

# Muestro el tiempo total de ejecución
print("Tiempo de ejecución:", round(fin - inicio, 4), "segundos")

