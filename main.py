import os
from Package_funciones.funciones_archivos import *
from Package_funciones.funciones_mensajes import *


def menu(path):

    mensaje_comienzo(1)
    mensaje_comienzo(0)
    lista = convertir_csv_lista(path)
    flag = False
    running = True
    while running:
        mensaje_programa(1)
        select = input("Ingrese una opcion A, B, C, D, X : ").upper()
        if select == "A":
            pass
        elif select == "B" and flag == True:
            pass
        elif select == "B" and flag == True:
            pass
        elif select == "B" and flag == True:
            pass
        elif select == "X":
            convertir_lista_csv(lista, path)
            mensaje_programa(3)
            break
            
        else:
            mensaje_programa(2)

        system("pause")
        system("cls")
        

menu("empleados.csv")



