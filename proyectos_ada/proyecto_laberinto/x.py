import os
import ramdom

        
def leer_mapa_desde_archivo(archivo):
        with open(archivo, "r") as file:
            pos_inicial = tuple(map(int, file.readline().split()))
            pos_final = tuple(map(int, file.readline().split()))
            # Lee el resto de las líneas y únelas en una cadena para el mapa
            mapa = ''.join(file.readlines())
            return pos_inicial, pos_final, mapa

mapa = leer_mapa_desde_archivo()
print(mapa)