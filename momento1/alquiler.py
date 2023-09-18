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
            if bicicletaE['estado'] == True:
                

                patida = input ("punto de partida: ")
                destino = input ("destino: ")
                n_alquiler = {
                    "id_bicicleta":bicicletaE["id"],
                    "color":bicicletaE["color"],
                    "user":va.userName,
                    "partida":patida,
                    "destino":destino
                }
                db.bicicletas
                db.h_alquiler.append(n_alquiler)
                print(c("green","\nalquiler agregado"))
                time.sleep(3)

                #cambio de estado en la bicicleta alquilada
                indice = va.buscar_indice(bicicletaE["id"],db.bicicletas)
                b = db.bicicletas[indice]
                b['estado'] = False
                y=True
            else:
                print(c("red","\nbicicleta no disponible\n"))
                time.sleep(2)
                os.system('cls')
        else:
            print(c("red","\nbicicleta no existe\n"))
            op2 = input("desea regresar al menu Y/N: ")
            if op2.lower() == "y":
                os.system('cls')
                import menus
                menus.Menu_second()
            else:
                os.system('cls')
                pass
            
            
        
   
    