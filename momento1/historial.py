import db
import validaciones as va
import time
import os
from colors import color as c

def Historial():
    os.system('cls')

    if len(db.h_alquiler) != 0:
        print(c("green","HISTORIAL DE ALQUILER\n"))
        for h in db.h_alquiler:
            print(c("yellow","usuario : ")+f"{h['user']}\n"+c("yellow","id bicileta : ")+f"{h['id_bicicleta']}\n"+c("yellow","color : ")+f"{h['color']}\n"+c("yellow","partida : ")+f"{h['partida']}\n"+c("yellow","destino : ")+f"{h['destino']}")
            print(c("green","_"*30))
            
        input(c("red","salir (presione enter)"))
        os.system('cls')
        import menus
        menus.Menu_second
            
    else:
        print(c("red","no hay historial de bicicletas alquiladas"))
        time.sleep(3)
        os.system('cls')
        import menus
        menus.Menu_second