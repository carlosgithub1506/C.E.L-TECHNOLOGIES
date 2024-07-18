import os
from Package_funciones.funciones_archivos import *
from Package_funciones.funciones_mensajes import *
from Package_funciones.funciones_generales import *


def menu(path):

    mensaje_comienzo(1)
    mensaje_comienzo(0)
    lista = convertir_csv_lista(path)
    print(lista)
    lista = normalizar_datos(lista)
    print(lista)
    flag = False
    running = True

    while running:
        mensaje_programa(1)
        select = input("Ingrese una opcion A, B, C, D, X : ").upper()
        if select == "A":
            lista = ingresar_datos(lista)
            flag = True
        elif select == "B": #and flag == True:
            lista_encontrados = buscar_claves(lista,"Genero", "MASCULINO")
            lista_encontrados = buscar_claves(lista_encontrados, "Tecnologia", "IA", "IOT")
            lista_encontrados = buscar_claves_rangos(lista_encontrados, "Edad", 24, 50)
            imprimir(f"Cantidad de empleados masculinos que votaron por IOT, IA es : {len(lista_encontrados)}")

        elif select == "C" and flag == True:
            pass
        elif select == "D" and flag == True:
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

