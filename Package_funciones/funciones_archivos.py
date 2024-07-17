import os

# convierte una lista de diccionarios a un archivo csv, recibe 2 parametros lista de diccionarios str(path) 
def convertir_lista_csv(lista:list, path:str)->None:

    if type(lista) == list:
        encabezados = lista[0].keys()
        with open(path, mode = "w", encoding = "utf-8") as archivo_csv:
            archivo_csv.write(",".join(encabezados)+ "\n")

            for diccionario in lista:
                lista_valores = diccionario.values()
                for valor in lista_valores:
                    archivo_csv.write(f"{valor},")
                archivo_csv.write(f"\n")


 # convierte un archivo csv a una lista de diccionarios, recibe 1 parametro str(path), retorna una lista                
def convertir_csv_lista(path:str)->list:

    if os.path.exists(path):
        lista = []
    
        with open(path, mode="r", encoding="utf-8") as archivo_csv:
            lista_lineas = archivo_csv.readlines()
            lista_claves = lista_lineas[0].strip().split(",")

            for i in range(1,len(lista_lineas)):
                diccionario = {}
                lista_valores = lista_lineas[i].strip().split(",")

                for j in range(len(lista_valores)):
                    if lista_valores[j] != "":
                        diccionario[lista_claves[j]] = lista_valores[j]
                lista.append(diccionario)
            return lista

convertir_csv_lista("empleados.csv")
