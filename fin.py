usuario = input()
print(f"BIENVENIDO,", usuario , "!!JUGUEMOS!!")

print(f"!!estas dentro de el juego, preciona la tecla '↑' para salir!!")

import readchar

while True:
    key = readchar.readkey()    

    if key == readchar.key.UP:
        print("Tecla '↑' presionada. saliendo del juego")
        break

    print(f"tecla '{key}' precionada.") 