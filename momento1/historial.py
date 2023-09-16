import db
import validaciones as va
import time
import os
from colors import color as c

def Historial():
    os.system('cls')

    if len(db.h_alquiler) != 0:
        for h in db.h_alquiler:
            print(f" usuario : {va.userName}\n id bicileta : {h.data_bicicleta.id}\n color : {h.data_bicicleta.color}\n partida : {h.partida}\n destino : {h.destino}")
            print("_"*50)
            
            salir = input("salir (presione enter)")
            
            if salir != None:
                os.system('cls')
                import menus
                menus.Menu_second
                
    else:
        print(c("red","no hay historial de bicicletas alquiladas"))
        time.sleep(3)
        os.system('cls')
        import menus
        menus.Menu_second