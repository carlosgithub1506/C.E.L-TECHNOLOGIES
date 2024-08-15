from os import system

# Imprime un mesaje que recibe por parametros dentro de 2 print que genera una especie de bloque 
def imprimir (parametro_1:str, parametro_2="")->None:

    print(f"\n{"*"*115}")
    print(f"\n{parametro_1} {parametro_2}")
    print(f"\n{"*"*115}")




# muestra un mensaje dependiendo la opcion que recibe por parametros(int)
def mensaje_programa(numero:int)->None:
   
    mensaje=""
    if numero == 1:    
        mensaje = f"\n{"*"*53}  Menu  {"*"*54}\n\nA) Realizar encuesta.\nB) Filtrar encuesta y cantidad de empleados que coinciden\nC) Filtrar encuesta y porcentaje de empleados que coinciden\nD) Filtrar encuesta y mostra el empleado con mayor edad.\nE) Mostrar todos los Empleados.\nX) Salir.\n\n{"*"*115} \n"
    elif numero == 2:
        mensaje = "*** Debe ingresar los datos solicitado en la opcion `A` ***"    
    elif numero == 3:
        mensaje=f"\nCerrando programa.....\n"
    elif numero == 6:
        mensaje=f"\nNo hay coincidencia.....\n" 
    elif numero == 7:
        mensaje=f"\n{"*"*51}  Sub-Menu  {"*"*51}\n\nA)Buscar Paciente por DNI.\nB)Modificar Nombre.\nC)Modificar Apellido.\nD)Modificar Edad.\nE)Modificar Altura.\nF)Modificar Peso.\nG)Modificar DNI.\nH)Modificar Grupo Sanguinio.\nX Salir del Sub-Menu.\n\n{"*"*115} \n"
    elif numero == 8:
        mensaje=f"\nCerrando Sub-Menu.....\n"

    else:
        mensaje = "\n**** Algo salio mal, ingrese los datos correctamente ****"        

    print(mensaje)    

    
# Muestra 2 mensaje dependiendo de la opcion que recibe por parametros(int)
def mensaje_comienzo(numero:int)->None:
    
    separador = "*"*115 
    mensaje=""

    if numero == 1:
        mensaje=f"Bienvenido a la encuesta de empleados de C.E.L TECHNOLOGY\n"  
    else:
        mensaje=f"Ingresando al Sistema. . . .\n"

    print(f"{separador}\n\n{mensaje}\n\n{separador}")
    system("pause")
    system("cls")  