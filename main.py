import os
import random
import readchar

class Juego:
    def _init_(self, ID_jugador, mapa, posicion_inicial, posicion_final):
        self.nb_jugador = ID_jugador
        self.mapa = mapa
        self.posicion_inicial = posicion_inicial
        self.posicion_final = posicion_final

    def cadena_a_matriz(self, mapa_str):
        filas = mapa_str.strip().split('\n')
        laberinto = []
        for fila in filas:
            caracteres = list(fila)
            laberinto.append(caracteres)
        return laberinto    
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_laberinto(self):
        self.limpiar_pantalla()
        for fila in self.mapa:
                print("".join(fila))
            #fila_sin_coordenadas = ' '.join(['.' if c.isdigit() else c for c in fila])
            #print(fila_sin_coordenadas)    

    def main_loop(self):
        px, py = self.posicion_inicial
        print('MUEVE TU JUGADOR CON LAS FLECHAS ↑,↓,←,→')        

        while True:
            self.mapa[py][px] = 'P'
            self.mostrar_laberinto()
            Key = readchar.readkey()

            nuevo_px, nuevo_py = px , py
            if Key == readchar.key.UP:
                nuevo_px  -= 1 
            elif Key == readchar.key.DOWN:        
                nuevo_px  += 1
            elif Key == readchar.key.LEFT:         
                nuevo_py  -= 1
            elif Key == readchar.key.RIGHT:
                nuevo_py += 1
            else:
                (px, py) == self.posicion_final
                print("¡Ganaste!")
                self.mostrar_laberinto()
                return
                    
class JuegoArchivo(Juego):
    def _init_(self, ID_jugador, mapa_folder, posicion_inicial, posicion_final):
        self.mapa_folder = mapa_folder
        super()._init_(ID_jugador, [], posicion_inicial, posicion_final)
        self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos = os.listdir(self.mapa_folder)
        if not archivos:
            raise FileNotFoundError("No se encontraron mapas en la carpeta especificada.")
        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(self.mapa_folder, nombre_archivo)
        with open(path_completo, "r") as archivo_mapa:
            mapa_str = archivo_mapa.read()
            self.mapa = self.cadena_a_matriz(mapa_str)
            inicio, fin = self.encontrar_inicio_y_fin(mapa_str)
            self.posicion_inicial = inicio
            self.posicion_final = fin

    def encontrar_inicio_y_fin(self, mapa_str):
        filas = mapa_str.strip().split('\n')
        inicio = (0, 0)
        fin = (len(filas[0]) - 1, len(filas) - 1)
        return inicio, fin

if __name__ == "_main_":
    ID_jugador = input("HOLA BIENVENIDO, por favor ingresa tu nombre: ")
    print(f"BIEN HECHO, {ID_jugador}")

    while True:
        respuesta = input("Para continuar (responde 'si' o 'no'): ").lower()
        if respuesta == "si":
            break
        elif respuesta == "no":
            print(f"Oh, tal vez en otro momento, {ID_jugador}. ¡Hasta luego!")
            exit()
        else:
            print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

    mapa_folder = (r"C:\Users\Juan Ruiz\Documents\Laberinto\Laberinto2\Mapas")

    posicion_inicial_mapa1 = (0, 0)
    posicion_final_mapa1 = (20, 20)
    juego_mapa1 = JuegoArchivo(ID_jugador, mapa_folder, posicion_inicial_mapa1, posicion_final_mapa1)
    juego_mapa1.main_loop()