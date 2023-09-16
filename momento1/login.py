import os
import db
from colors import color as c
import validaciones as va

def Login():
    os.system('cls')
    username = input("Username: ")
    user = va.validar_usuario_name(username,db.users)
    if user != None:
        bol = 0
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
        print(c("red","USUARIO  no esta registrado\n"))
            
            
            
            