import os
import readchar


class Juego :

    def __laberinto__(self, mapa_str):
        return list(map(list, self.mapa_str.strip().split('\n')))

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(self,mapa):
        self.clear_screen()
        print('MUEVE TU JUGADOR CON LAS FLECHAS ↑,↓,←,→')
        for fila in mapa:
            print("".join(fila))

    
    def __main_loop__(self, mapa_str ,p_inicio, p_final ) :
        px, py = p_inicio
        fx, fy = p_final
        mapa_str[px][py] = 'P'
        print('MUEVE TU JUGADOR CON LAS FLECHAS ↑,↓,←,→')

        while (px, py) != (fx, fy):
            self.montrar_mapa(self.mapa)
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

            if (0 <= nuevo_px < len(self.mapa)) and (0 <= nuevo_py < len(self.mapa[0])) and self.mapa[nuevo_px][nuevo_py] != '#':
                self.mapa[px][py] = '.'
                px, py = nuevo_px, nuevo_py
                self.mapa[px][py] = 'P'  
        
            
            if (0 <= nuevo_px < len(self.mapa)) and (0 <= nuevo_py < len(self.mapa[0])) and self.mapa[nuevo_px][nuevo_py] != '#' and (nuevo_px, nuevo_py) == self.posicion_final:
                self.clear_screen()
                print("!!FIN DE JUEGO,FELICITACIONES!!")

        self.mapa = mapa_str()

    posicion_inicial=  (0, 0)
    posicion_final = (19, 19)  


