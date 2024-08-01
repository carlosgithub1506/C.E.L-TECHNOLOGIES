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
        select = input("Ingrese una opcion A, B, C, D, X : ").upper()
        if select == "A":

            lista = ingresar_datos(lista)
            flag = True

        elif select == "B" and flag == True:

            lista_encontrados = buscar_claves(lista,"Genero", "MASCULINO")
            lista_encontrados = buscar_claves(lista_encontrados, "Tecnologia", "IA", "IOT")
            lista_encontrados = buscar_claves_rangos(lista_encontrados, "Edad", 24, 51)
            imprimir(f"Cantidad de empleados masculinos que votaron por IOT, IA y edad entre 25 y 50 años es : {len(lista_encontrados)}")

        elif select == "C" and flag == True:

            lista_busqueda =  buscar_claves(lista, "Genero", "MASCULINO", "OTRO")
            lista_busqueda =  buscar_claves(lista_busqueda, "Tecnologia", "RV", "IOT")
            lista_busqueda =  buscar_claves_rangos(lista_busqueda, "Edad", 32, 41)
            porcentaje = len(lista_busqueda) / len(lista) * 100
            imprimir(f"Porcentaje de empleados genero Otro, Masculino que votaron por IOT, RV es : {round(porcentaje)} %")

        elif select == "D" :#and flag == True:

            lista_busqued = buscar_claves(lista,"Genero", "MASCULINO")
            dicc_mayor = buscar_mayor(lista_busqued, "Edad")
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

