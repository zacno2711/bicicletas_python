
import os 
from colors import color as c
import validaciones as va
import db
import time

def Registro():
    os.system('cls')
    x = False
    while not x:
        count = 0
        while count < 3:
            print(c("cyan","REGISTRO DE USUARIO\n"))
            name = input("Nombre :")
            if va.validar_nombre(name):
                count+=1
            else:
                count = 0
                break 

        
        while count < 3: 
            psw = input("Contraseña: ")
            if va.validar_password(psw):
                user = {"name":name,"psw":psw}
                db.users.append(user)
                print(c("green","\nUSUARIO CREADO"))
                time.sleep(2)
                print("\n")
                import menus
                menus.Menu_home()
            else:
                count += 1

        
        if count == 3:
            print(c("red","\nREGISTRO DE USUARIO CANCELADO"))
            time.sleep(2)
            import menus
            menus.Menu_home()