

def validate_str(string:str)->bool:

    retorno = False
    if string.isalpha() == True:
        retorno = True
    return retorno


def validate_int(numero:int)->bool:
    retorno = False
    if numero.isdigit() == True and (int(numero) > 17 and int(numero) < 100):
        retorno = True
    return retorno


def validate_str_tipos(texto:str ,lista_tipos:list)->bool:
    retorno = False
    if texto.isalpha() == True:
        for tipo in lista_tipos:
            if tipo == texto:
                retorno = True
                break
    return retorno




