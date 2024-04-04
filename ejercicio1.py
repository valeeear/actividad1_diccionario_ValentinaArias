mi_diccionario =  {}
import os

ls_categoria1 = []
ls_categoria2 = []  
sw = True
def fnt_limpiar():
    os.system('cls')
    print('\nBienvenido al sistema de calificación de estudiantes')
    print('Categoría registrados: ',ls_categoria1)
    print('Categoría pendientes: ',ls_categoria2)



def fnt_agregar(diccionario, id, nombre_completo, edad, estrato):
    if id == '' or nombre_completo == ''  or edad == '' or estrato == '':
        enter = input('Debe diligenciar toda la información solicitada >ENTER<')
        
        
def fnt_selector(op):
    if op == '1':
        os.system('cls')
        id = input('Id:  ')
        nombre_completo = input('Nombre:  ')
        edad = input('Edad:  ')
        estrato = input('Estrato:  ')
        fnt_agregar(mi_diccionario, id, nombre_completo, edad, estrato)
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nInformación estudiantes: ', len(mi_diccionario), '\n')
        
        
        
    