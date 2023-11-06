import os
import readchar

print(f"preciona la tecla 'N' hasta que te indique parar!!")

def ciclo():    

    for i in range(1,51):

        key = readchar.readchar()
        contador = -1
        if key <= 'n':
            contador +=i
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"Vamos en el numero: " , contador)
        
ciclo()