
import vaimport os 
from colors import color as clidaciones as va
import db

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
                print(c("green","USUARIO CREADO"))
                print("\n")
                import menus
                menus.Menu_home()
            else:
                count += 1

        
        if count == 3:
            print(c("red","REGISTRO DE USUARIO CANCELADA"))
            import menus
            menus.Menu_home()