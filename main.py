from mapa_clases import Juego

import os
import random


print("ingresa tu ID de usuario: ")

usuario = input()

print(f"BIENVENIDO,", usuario , "!!JUGUEMOS!!")

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.archivos_mapa = os.listdir(path_a_mapas)

    def cargar_mapa_al_azar(self):
        if self.archivos_mapa:
            nombre_archivo = random.choice(self.archivos_mapa)
            path_completo = f"{self.path_a_mapas}/{nombre_archivo}"
            with open(path_completo, 'r') as archivo_mapa:
                contenido_mapa = archivo_mapa.read()
                return contenido_mapa
        else:
                return "No se encontraron mapas en la carpeta especificada."
        
    def leer_mapa(self, nombre_archivo):
        path_completo = f"{self.path_a_mapas}/{nombre_archivo}"
        with open(path_completo, 'r') as archivo_mapa:
            lineas = archivo_mapa.readlines()
            contenido_formateado = ''.join(lineas).strip()
            return contenido_formateado    

        
        

path_a_mapas_ejemplo = 'C:/Users/Juan Ruiz/Documents/Laberinto/Laberinto2/Mapas/'
juego = JuegoArchivo(path_a_mapas_ejemplo)
mapa_al_azar = juego.cargar_mapa_al_azar()
print(mapa_al_azar)