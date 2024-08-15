import os
from Package_funciones.funciones_archivos import *
from Package_funciones.funciones_mensajes import *
from Package_funciones.funciones_generales import *


def menu(path):

    mensaje_comienzo(1)
    mensaje_comienzo(0)
    lista = convertir_csv_lista(path)
    lista = normalizar_datos(lista)
    flag = False
    running = True

    while running:
        mensaje_programa(1)
        select = input("Ingrese una opcion A, B, C, D, E, X : ").upper()
        print(f"\n{"*"*115}\n")

        if select == "A":

            lista = ingresar_datos(lista)
            flag = True

        elif select == "B" and flag == True:
            lista_filtrada = mostrar_menu_ordenar(lista)
            mostrar_lista_diccionario(lista_filtrada)
            imprimir(f"Cantidad de empleados: {len(lista_filtrada)}")

        elif select == "C" and flag == True:

            lista_filtrada = mostrar_menu_ordenar(lista)
            mostrar_lista_diccionario(lista_filtrada)
            porcentaje = len(lista_filtrada) / len(lista) * 100
            imprimir(f"Porcentaje de empleados es : {round(porcentaje)} %")

        elif select == "D" and flag == True:
            lista_filtrada = mostrar_menu_ordenar(lista)
            dicc_mayor = buscar_mayor(lista_filtrada, "Edad")
            mostrar_diccinario(dicc_mayor, True)

        elif select == "E" and flag == True:
            
            mostrar_lista_diccionario(lista)

        elif select == "X":

            convertir_lista_csv(lista, path)
            mensaje_programa(3)
            break
            
        else:
            mensaje_programa(2)

        system("pause")
        system("cls")
    
menu("empleados.csv")

