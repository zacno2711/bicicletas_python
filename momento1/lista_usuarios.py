import db 
import os
from colors import color as c

def Lista_usuarios():
    os.system('cls')
    print(c("green","LISTA DE USUARIOS\n"))
    for u in db.users:
        print(f"nombre : {u['name']} ")
        print(c("green","_"*10))
    
    input(c("red","press enter para salir"))
    os.system('cls')
    import menus
    menus.Menu_second