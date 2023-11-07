import os
import readchar


def laberinto(mapa_str):
    return list(map(list, mapa_str.strip().split('\n')))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def montrar_mapa(mapa):
  clear_screen()
  print('MUEVE TU JUGADOR CON LAS FLECHAS ↑,↓,←,→')
  for fila in mapa:
      print("".join(fila))
  




def main_loop(mapa_str, p_inicio, p_final):
    px, py = p_inicio
    fx, fy = p_final
    mapa_str[px][py] = 'P'
    print('MUEVE TU JUGADOR CON LAS FLECHAS ↑,↓,←,→')

    while (px, py) != (fx, fy):
        montrar_mapa(mapa)
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

        if (0 <= nuevo_px < len(mapa)) and (0 <= nuevo_py < len(mapa[0])) and mapa[nuevo_px][nuevo_py] != '#':
            mapa[px][py] = '.'
            px, py = nuevo_px, nuevo_py
            mapa[px][py] = 'P'  
        
            
        if (0 <= nuevo_px < len(mapa)) and (0 <= nuevo_py < len(mapa[0])) and mapa[nuevo_px][nuevo_py] != '#' and (nuevo_px, nuevo_py) == final:
            clear_screen()
            print("!!FIN DE JUEGO,FELICITACIONES!!")
            break
        
        
        

mapa_str = """
..###################
....#.....#.........#
#.#.#.#.#######.#.#.#
#.#...#.#.......#.#.#
###.###.#####.#####.#
#...#.....#.#...#.#.#
#.#.#.###.#.#.###.###
#.#.#.#.#.......#...#
#.#####.#.#########.#
#...#.....#.#.#.....#
#.###.#.###.#.#.#.###
#.#.#.#.#.....#.#.#.#
#.#.#.#.###.###.###.#
#.#...#.......#.....#
###.###.#.###.###.###
#...#...#...#.......#
#####.###.###.#####.#
#...#.#...#.....#...#
#.#.#.#####.#####.###
#.#.....#.....#.....#
###################.#
"""

mapa= laberinto(mapa_str)
inicio = (0, 0)
final = (20, 19) 

if (0 <= inicio[0] < len(mapa) and 0 <= inicio[1] < len(mapa[0]) and 
    0 <= final[0] < len(mapa) and 0 <= final[1] < len(mapa[0])):
    
    main_loop(mapa,(0,0), (len(mapa)-1, len(mapa[0])-1))



    
