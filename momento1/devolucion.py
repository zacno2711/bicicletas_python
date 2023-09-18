# import db
# import time
# from colors import color as c
# import validaciones as va
# import os

# def Devolucion ():
#     os.system('cls')
#     if va.validar_bicicleta_estado():

#         for b in db.h_alquiler:
#             print(c("yellow","usuario : ")+f"{b['user']}\n"+c("yellow","id bicileta : ")+f"{b['id_bicicleta']}\n"+c("yellow","color : ")+f"{b['color']}\n"+c("yellow","partida : ")+f"{b['partida']}\n"+c("yellow","destino : ")+f"{b['destino']}")
#             print(c("green","_"*30))

#         op = input(c("\nyellow","digite el id de la bicicleta que va devolver: "))
#         indice = va.buscar_indice(op,db.bicicletas)
#         b = db.bicicletas[indice]
#         b['estado'] = True
#         print(c("green","\nBicicleta devuelta"))
#         time.sleep(3)
#         os.system('cls')
#         import menus
#         menus.Menu_second
#     else:
#         print(c("red","No hay bicicletas alquiladas para devolver"))
#         time.sleep(3)
#         os.system('cls')
#         import menus
#         menus.Menu_second
