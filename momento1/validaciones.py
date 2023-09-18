import db 
import re
from colors import color as c

    
def validar_user(name,users):
    for user in users:
        if user["name"] == name:
            return user
        
        
def validar_nombre(name):
    if len(name)<3:
        print(c("red","Minimo 3 caracteres"))
        return True
    else :
        user =  validar_user(name,db.users)
        if user != None:
            print(c("red","Nombre de usuario ya existe, intente con otro"))
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
    for x in db.bicicletas:
        if x["id"] == int(op):
            return x

def validar_bicicleta_estado ():
    for b in db.bicicletas:
        if b["estado"]==False:
            return True
    
def buscar_indice(id,lista): 
    for index, diccionario in enumerate(lista):
        if diccionario.get("id") == id:
            return index     
 
userName = ""
