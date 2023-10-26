import os
import random
from readchar import readkey, key

# Parte 1: Bienvenida al juego
print("Introduce tu nombre")
nombre = input()
print(f"¡Hola {nombre}! Bienvenido al juego del laberinto")

print(""" 
      #######     ####   ###     #####     ###    ###    #########
    ####   ####   ####   ###    ### ###    ###  ###      ###
      ####        #####  ###   ###   ###   ######        #######
  ###    ####     ### ## ###   #########   ######        ###
   ####   #####   ###  #####   ###   ###   ###   ###     ###
     ########     ###  #####   ###   ###   ###    ####   ######### """)

# Parte 2: Juego de teclas
print("Presiona cualquier tecla (Flecha arriba para salir):")

while True:
    k = readkey()

    if k == key.UP:  # Verifica si se presionó la tecla de flecha hacia arriba (↑)
        print("Tecla de flecha hacia arriba presionada. Saliendo del programa.")
        break
    else:
        print(f"Tecla presionada: {k}")

# Parte 3: Juego de números
from readchar import readkey

number = 0

def borrar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

while number <= 50:
    borrar_consola()
    print("Presiona 'n' para aumentar el número. Presiona cualquier otra tecla para salir.")
    print(f"Número: {number}")
    llave = readkey()

    if llave == 'n':
        number += 1
    else:
        break

# Parte 4: Juego de laberinto
import time

# Mapa del laberinto
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

# Función para convertir el mapa en una matriz de caracteres
def crear_laberinto(laberinto_str):
    filas = laberinto_str.split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz

# Función para limpiar la pantalla y mostrar el laberinto
def mostrar_laberinto(matriz):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

    for fila in matriz:
        print("".join(fila))  # Imprime cada fila del laberinto

# Función principal del juego
def main_loop(laberinto_mapa, posicion_inicial, posicion_final):
    laberinto_matriz = crear_laberinto(laberinto_mapa)
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        mostrar_laberinto(laberinto_matriz)
        laberinto_matriz[py][px] = 'P'

        # Leer entrada del usuario
        movimiento = input("Presiona una tecla de flecha para mover al jugador (q para salir): ")

        if movimiento == 'q':
            break
        elif movimiento == 'w':
            if py - 1 >= 0 and laberinto_matriz[py - 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                py -= 1
        elif movimiento == 's':
            if py + 1 < len(laberinto_matriz) and laberinto_matriz[py + 1][px] != '#':
                laberinto_matriz[py][px] = '.'
                py += 1
        elif movimiento == 'a':
            if px - 1 >= 0 and laberinto_matriz[py][px - 1] != '#':
                laberinto_matriz[py][px] = '.'
                px -= 1
        elif movimiento == 'd':
            if px + 1 < len(laberinto_matriz[0]) and laberinto_matriz[py][px + 1] != '#':
                laberinto_matriz[py][px] = '.'
                px += 1

    mostrar_laberinto(laberinto_matriz)

# Coordenadas iniciales y finales
posicion_inicial = (0, 0)
posicion_final = (len(laberinto.split('\n')[0]) - 1, len(laberinto.split('\n')) - 1)

# Iniciar el juego
main_loop(laberinto, posicion_inicial, posicion_final)

# Parte 5: Juego de laberinto con archivos
class Juego:
    def __init__(self, carpeta_mapas):
        self.carpeta_mapas = carpeta_mapas
        self.mapa = ""
        self.inicio = (0, 0)
        self.final = (0, 0)

    def cargar_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.carpeta_mapas)
        archivo_aleatorio = random.choice(archivos_mapas)
        ruta_mapa = os.path.join(self.carpeta_mapas, archivo_aleatorio)
        with open(ruta_mapa, 'r') as archivo:
            self.mapa = archivo.read()

    def encontrar_inicio_final(self):
        lineas = self.mapa.strip().split('\n')
        self.inicio = (0, 0)
        self.final = (len(lineas) - 1, len(lineas[0]) - 1)

    def mostrar_laberinto(self):
        for fila in self.mapa:
            print(fila)

    def jugar(self):
        while True:
            self.mostrar_laberinto()
            # Implementa el movimiento del jugador y otras lógicas del juego aquí
            pass

# Crear una instancia del juego
carpeta_mapas = "mapas"
juego = Juego(carpeta_mapas)

# Cargar un mapa aleatorio
juego.cargar_mapa_aleatorio()
juego.encontrar_inicio_final()

# Jugar el juego
juego.jugar()

# Mensaje de felicitaciones
print(f"Felicidades, {nombre} ¡superaste el juego del laberinto!")
