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
            mensaje = "Ingrese tecnologia  (IA, RV, IOT): "
            lista_tipos = ["IA","RV","IOT"]
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

def buscar_mayor(lista:list[dict], clave:str)->dict:
    flag_2 = True
    dicc_mayor = None
    for diccionario in lista:
        if flag_2 == True or diccionario[clave] > dicc_mayor[clave]:
            dicc_mayor = diccionario 
            flag_2 = False
    return dicc_mayor



# obtener_claves_dict: Recibe un diccionario y retorna una lista con las claves de un diccionario | bool
def obtener_claves_dict(diccionario:dict)->list|bool:
    retorno = False
    if type(diccionario) == dict: 
        lista_claves = list(diccionario.keys())
        retorno = lista_claves
    return retorno


# obtener_valores_dict recibe un diccionario y retorna una lista con los valores de un diccionario | bool
def obtener_valores_dict(diccionario:dict)->list | bool:
    retorno = False
    if type(diccionario) == dict: 
        lista_valores = list(diccionario.values())
        retorno = lista_valores
    return retorno




# convertir_a_str: recibe una lista, convierte  cada elemento de la lista a str, lo concadena y da formato a una variable que luego retorna | puede retorna un string con un caracter repetidos 115 veces 
def convertir_a_str(lista:list,caracter="*")->str:

    string = f"{caracter*115}\n"
    separador = " | "

    if type(lista) == list:
        for elemento in lista:
            elemento = str(elemento)
            if len(elemento) < 1:
                string += f"{separador}{elemento:<3}"

            elif len(elemento) >3  and len(elemento)< 10:
                string += f"{separador}{elemento:<10}"

            else:
                string += f"{separador}{elemento:<12}"

        string += f"{separador}"
    return string 



# mostrar_paciente: recibe un diccionario y un booleano segun el estado del booleano va hacer el formato que se va a mostrar, hace uso de otras funciones para dar formato
def mostrar_diccinario(empleado:dict, mostrar_un_elemento:bool) ->None:
    
    mensaje = "hubo un error"

    if type(empleado) == dict:
        lista_valores = obtener_valores_dict(empleado)
        string_valores = convertir_a_str(lista_valores,"-")
        mensaje = string_valores

        if  mostrar_un_elemento:
            lista_claves = obtener_claves_dict(empleado)
            string_claves = convertir_a_str(lista_claves)
            base_tabla=convertir_a_str(False)     
            mensaje=f"{string_claves}\n{string_valores}\n{base_tabla}"

    print(mensaje)


# mostrar_lista_paciente recibe una lista de diccionario la recorrre y muestra todos los elementos en formato de tabla, hace usos de otras funciones para obtener claves de un diccionario y formatear y mostrar
def mostrar_lista_diccionario(lista:list[dict])->None:

    if type(lista) == list and  len(lista) > 0:
        lista_claves = obtener_claves_dict(lista[0])
        string_claves = convertir_a_str(lista_claves)
        print(string_claves)

        for empleado in lista:
            mostrar_diccinario(empleado,False)
        base_tabla=convertir_a_str(False)                
        print(base_tabla)


