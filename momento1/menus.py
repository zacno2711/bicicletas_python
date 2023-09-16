import os
from colors import color as c
import validaciones as va


def Menu_home():
    os.system('cls')
    print(c("cyan","Home\n"))
    opMenu1 = input(f"{c ('yellow','1.')} REGISTRO \n{c ('yellow','2.')} LOG IN \n--> ")
    if opMenu1 == "1":
        from registro import Registro
        Registro()
        
    elif opMenu1 == "2":
        from login import Login
        os.system('cls')
        Login()
    else:
        print("opcion errada")
        
def Menu_second():
    t = True
    while t:
        os.system('cls')
        print(f"\nUSER ----> {c('green',f'{va.userName}')}\n")

        opMenu = input(f"{c ('yellow','1.')} ALQUILAR BICICLETA \n{c ('yellow','2.')} HISTORIAL DE ALQUILER \n{c ('yellow','3.')} LISTA DE USUARIOS \n{c ('yellow','Other key.')} Salir \n--> ")

        if opMenu == "1":
            import alquiler
            alquiler.Alquiler()
            
        elif opMenu == '2':
            import historial
            historial.Historial

        elif opMenu == "3":
            import lista_usuarios
            lista_usuarios.Lista_usuarios()
        else: 
            op1= input(c("red",f"{va.userName}, deseas cerrar sesion? Y/N: "))
            if op1.lower()=="y":
                va.userName = ""
                Menu_home()
            else: 
                pass