import db 
import os
from colors import color as c

def Lista_bicicletas():
    os.system('cls')
    print(c("green","LISTA DE BICICLETAS\n"))
    for b in db.bicicletas:
        print(f"id : {b['id']} ")
        print(f"color : {b['color']} ")
        print(f"disponible : {b['estado']} ")
        
        print(c("green","_"*10))
    
    input(c("red","press enter para salir"))
    os.system('cls')
    import menus
    menus.Menu_second