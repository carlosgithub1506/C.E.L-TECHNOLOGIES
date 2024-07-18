from Package_get_validate.funciones_validate import *

def get_str(mensaje_input:str)->str|bool:
    retorno = ""
    contador = 3
    
    while contador > 0:

        if contador == 0:
            retorno = False
            break
        elif contador == 3:
            texto = input(mensaje_input).strip()
            validacion = validate_str(texto)
        else:
            texto = input(f"{mensaje_input}, oportunidades restantes {contador}: ").strip()
            validacion = validate_str(texto)

        if validacion == True:
            retorno = texto.capitalize()
            break
        contador -= 1
    
    return retorno



def get_int(mensaje:str)->int|bool:
    retorno = False
    contador = 3
    while contador > 0:
        if contador == 3:
            numero = input(mensaje).strip()
            validacion = validate_int(numero)
        else:
            numero = input(f"{mensaje}. intentos restantes {contador}: ").strip()
            validacion = validate_int(numero)

        if validacion == True :
            retorno = int(numero)
            break
        contador -= 1
    return retorno


def get_str_tipo(mensaje_input:str, lista_tipos:list)->str|bool:
    retorno = ""
    contador = 3
    
    while contador > 0:

        if contador == 0:
            retorno = False
            break
        elif contador == 3:
            texto = input(mensaje_input).strip().upper()
            validacion = validate_str_tipos(texto ,lista_tipos)
        else:
            texto = input(f"{mensaje_input}, oportunidades restantes {contador}: ").strip().upper()
            validacion = validate_str_tipos(texto ,lista_tipos)

        if validacion == True:
            retorno = texto
            break
        contador -= 1
    
    return retorno


