import os
import db
from colors import color as c
import validaciones as va
import time

def Login():
    t = True
    bol = 0
    while t:
        os.system('cls')
        username = input("Username: ")
        user = va.validar_user(username,db.users)
        print(user)
        
        if user != None:
            while bol < 3:
                psw = input("Contraseña: ")
                if psw != user["psw"]:
                    bol += 1
                    print(c("red","\nContraseña incorrecta\n"))
                else:
                    va.userName = user["name"]
                    from menus import Menu_second
                    Menu_second()
        else: 
            os.system('cls')
            bol += 1
            print(c("red","USUARIO  no esta registrado, intente con otro\n"))
            time.sleep(3)


            
            
            
            