from Package_get_validate.funciones_get import *

def crear_empleado(lista_claves:list, lista_valores:list)->dict:
    diccionario = {}
    for i in range(len(lista_claves)):
        diccionario[lista_claves[i]] = lista_valores[i]
    return diccionario



def ingresar_datos(lista:list[dict])->list[dict]:

    lista_valores = []
    lista_claves = list(lista[0].keys())
    for clave in lista_claves:

        if clave == "Nombre":
            mensaje = "Ingrese su nombre: "
            valor = get_str(mensaje)

        elif clave == "Edad":
            mensaje = "Ingrese edad mayor a 18: "
            valor = get_int(mensaje)

        elif clave == "Genero":
            mensaje = "Ingrese su genero (MASCULINO - FEMENINO - OTRO): "
            lista_tipos = ["MASCULINO", "FEMENINO", "OTRO"]
            valor = get_str_tipo(mensaje, lista_tipos)

        elif clave == "Tecnologia":
            mensaje = "Ingrese tecnologia  (IA, RV,RA, IOT): "
            lista_tipos = ["IA","RV","RA","IOT"]
            valor = get_str_tipo(mensaje, lista_tipos)

        if valor != False:
            lista_valores.append(valor)
        else:
            print("Dato ingresado es incorrecto")
            break
        
    if len(lista_valores) == len(lista_claves):
        diccionario = crear_empleado(lista_claves, lista_valores)
        lista.append(diccionario)

    return lista



def buscar_claves(lista:list, keys:str, valor:str, valor_2="")->list:
    lista_encontrados = []
    for dicc in lista:
        if dicc[keys] == valor or dicc[keys] == valor_2 :
            lista_encontrados.append(dicc)
    return lista_encontrados


def buscar_claves_rangos(lista:list, keys:str, rango_1:int, rango_2:int)->list:
    lista_encontrados = []
    for dicc in lista:
        if dicc[keys] > rango_1 and dicc[keys] < rango_2 :
            lista_encontrados.append(dicc)
    return lista_encontrados


def normalizar_datos(lista:list[dict])->list:
    for dicc in lista:
        for clave in list(dicc.keys()):
            valor = dicc[clave]
            if valor.isdigit() == True:
                dicc[clave] = int(valor)
    return lista