import db 
import os
def Lista_usuarios():
    for u in db.users:
        print(f"nombre : {u.nombre}\n ")
        print("_"*20)
    
    input("press enter para salir")
    os.system('cls')
    import menus
    menus.Menu_second