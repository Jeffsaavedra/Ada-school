# EJERCICIO AÑOS BISIESTOS

# las funciones realizan actividades específicas
# las variables guardan información
año = int(input("Ingresa un año ")) # solicitar al usuario ingresar un año y guardarlo en la variable año

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                                       # (año % 100 % 4 == 0)
    print("Es un año bisiesto") # El print se utiliza para mostrar lo que queremos en la consola cuando no usamos una función
                                # Si queremos ver el resultado de una función usamos return "lo que queremos visualizar" al final de la función
else:
    print("No es un año bisiesto")   
                                    
# 1600 tenemos que quitarle los 2 ultimos (00) == 1600 / 100 == 16
# 1971 / 100 == 19 residuo 71

# EJERCICIO TRES NUMEROS

num1 = int(input("Ingresa tú número 1/3: ")) #solicita un número de 3 por ejemplo el 8
num2 = int(input("Ingresa tú número 2/3: ")) #solicita un número de 3 por ejemplo el 5
num3 = int(input("Ingresa tú número 3/3: ")) #solicita un número de 3 por ejemplo el 4

                                  # Al inicio num1 = 8 ; num2 = 5 ; num3 = 4 
          
                                  # Compara sí num1 es mayor que num2 y sí es así los cambia de variable
if num2 < num1:                   # sí num2 = 5 < num1 = 8
    num1 , num2 = num2 , num1     # entonces 5 deja de ser num2 para convertirse en num1 y 8 deja de ser num1 para ser num2

    # después del primer if num1 = 5 ; num2 = 8 ; num3 = 4
    
                                  # Compara sí num3 es mayor que el actual num2 y sí es así los cambia de variable
if num3 < num2:                   # sí num3 = 4 < num2 = 8
    num2 , num3 = num3 , num2     # entonces 4 deja de ser num3 para convertirse en num2 y 8 deja de ser num2 para ser num3

    # después del segundo if num1 = 5 ; num2 = 4 ; num3 = 8 
    
                                  # Compara sí el actual num1 es mayor que el actual num2 y sí es así los cambia de variable
if num2 < num1:                   # sí num2 = 4 < num1 = 5
    num1 , num2 = num2 , num1     # entonces 4 deja de ser num2 para convertirse en num1 y 5 deja de ser num1 para ser num2
                                  
    # después del tercer if num1 = 4 ; num2 = 5 ; num3 = 8 

print(num1 , num2 , num3)

# EJERCICIO LECTURA DE CARACTERES

# Leer una letra desde la entrada estándar
letra = input("Ingresa cualquier letra del alfabeto: ")

# Verificar si la letra es minúscula o mayúscula
if letra.islower():
    print("minuscula")
elif letra.isupper():
    print("mayuscula")

# Verificar si la letra es vocal o consonante
vocales = "AEIOUaeiou"
if letra in vocales:
    print("vocal")
else:
    print("consonante")