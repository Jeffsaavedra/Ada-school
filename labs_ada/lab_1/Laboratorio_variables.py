nombre = "Jeff"
edad = 21
calificación = 99.98
resultado = True

mensaje = "Hola soy " + nombre + " tengo " + str(edad) + " mi calificación es: " + str(calificación) + " ¿aprové? " + str(resultado)

print(mensaje)

# Límite de los enteros
    # Son flexibles y pueden terminar siendo arbitrariamente grandes por tanto la memoria se ajusta según su tamaño
    # Podemos usar "import sys" para determinar el entero más grande representado el tú implementación de Python

# Límite de los flotantes
    # Pueden representar números muy grandes o muy pequeños pero con una precisión limitada a un támaño definido de su parte fracional 

numero = int(input(f'Ingresa el número de pares que quieres sumar: '))

formula = ((numero + 1)* numero)
print(f"La suma de los primeros {numero} pares es: {formula} ")