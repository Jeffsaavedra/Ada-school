import random
import os

class Juego:
    def __init__(self, carpeta_mapas):
        self.carpeta_mapas = carpeta_mapas
        self.mapa = ""
        self.inicio = (0, 0)
        self.final = (0, 0)

    def cargar_mapa_aleatorio(self):
        # Obtener una lista de archivos de mapas en la carpeta
        archivos_mapas = os.listdir(self.carpeta_mapas)

        # Elegir un archivo aleatorio
        archivo_aleatorio = random.choice(archivos_mapas)

        # Componer la ruta completa al archivo de mapa
        ruta_mapa = os.path.join(self.carpeta_mapas, archivo_aleatorio)

        # Leer y cargar el mapa desde el archivo
        with open(ruta_mapa, 'r') as archivo:
            self.mapa = archivo.read()

    def encontrar_inicio_final(self):
        # Extraer las coordenadas de inicio y final del mapa
        lineas = self.mapa.strip().split('\n')
        self.inicio = (0, 0)  # Define las coordenadas de inicio
        self.final = (len(lineas) - 1, len(lineas[0]) - 1)  # Define las coordenadas finales

    def mostrar_laberinto(self):
        # Mostrar el laberinto actual
        for fila in self.mapa:
            print(fila)

    def jugar(self):
        # Lógica principal del juego
        while True:
            self.mostrar_laberinto()
            # Implementa el movimiento del jugador y otras lógicas del juego aquí
            pass