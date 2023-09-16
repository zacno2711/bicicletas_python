import validaciones as va
import db
from colors import color as c
import os
import time


def Alquiler():
    os.system('cls')
    y= False
    while not y:
        print(c("cyan","ALQUILER DE BICICLETAS \n"))
        
        op = input("que bicicleta deseas alquilar? digite su id: ")
        bicicletaE = va.validar_bicicleta(op)
        if bicicletaE:
            
            patida = input ("punto de partida: ")
            destino = input ("destino: ")
            n_alquiler = {
                "data_bicicleta":bicicletaE,
                "user":va.userName,
                "partida":patida,
                "destino":destino
            }
            db.h_alquiler.append(n_alquiler)
            print(c("green","alquiler agregado"))
            time.sleep(3)
            y=True
        else:
            print(c("red","la bicicleta no existe\n"))
            op2 = input("desea regresar al menu Y/N: ")
            if op2.lower() == "y":
                os.system('cls')
                import menus
                menus.Menu_second()
            else:
                os.system('cls')
                pass
            
            
        
   
    