import db 
import re
from colors import color as c

def validar_nombre (name, users):
    bol = False
    if not validar_usuario_name(name, users):
        bol = True
    else:
        print(c("red","usuario registrado"))
        bol = False
    if bol:
        return True
    else:
        return False
    

    
def validar_usuario_name(name,users):
    bol = False
    for x in users:
        if name == x["name"]:
            bol = True
    if bol:
        return True
    else:
        return False

def validar_password(psw):
    if len(psw) >= 5:
        patron = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{5,}$'
        if re.match(patron, psw):
            return True
        else:
            print(c("red","- Debe contener al menos una letra mayúscula o minúscula. \n- Debe contener al menos un dígito numérico.")) 
            return False
    else:
        print(c("red","- Debe contener al menos 5 caracteres"))
        return False
    
def validar_bicicleta(op):
    bol = False
    for x in db.users:
        if op == x["id"]:
            bol = True
    if bol == False:
        return False
    else:
        return x

        
    
userName = ""