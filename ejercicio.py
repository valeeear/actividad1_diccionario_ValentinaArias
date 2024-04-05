mi_diccionario = {}
pendiente_lista = []
import os

def fnt_agregar(mi_diccionario, id, nombre, apellidos, edad, estrato, sexo):
    if id == '' or nombre == '' or apellidos == '' or edad == '' or estrato == '' or sexo == '':
        enter = input('Debes diligenciar toda la información >ENTER<')
    else:
        edad = int(edad)
        estrato = int(estrato)
        if sexo == 'M' and (edad >=15 and edad <=25) and (estrato >=1 and estrato <=2):
            mi_diccionario[id] = {'Nombre' : nombre, 'Apellidos': apellidos, 'Edad': edad, 'Estrato': estrato, 'Sexo': sexo}
            enter = input(f'\n La persona {nombre} ha sido registrada. >ENTER<')
        elif sexo == 'F' and (edad >=20 and edad <=35) and (estrato >=1 and estrato <=4):
            mi_diccionario[id] = {'Nombre': nombre, 'Apellidos': apellidos, 'Edad': edad, 'estrato': estrato, 'Sexo': sexo}
            enter = input(f'\nLa persona (nombre) ha sido registrada con éxito «ENTER>') 
        else: 
            pendiente_lista. append(nombre)
        enter = input(f'Indebido a que no cumples con los requerimientos ha sido registrada en la lista de espera con exito «ENTER>')
        
        
def fnt_selector(op):
    global mi_diccionario
    global sw
    if op == '1':
        id = input('Id:  ')
        nombre = input('Nombre:  ')
        apellidos = input('Apellidos:  ')
        edad = input('Edad:  ')
        estrato = input('Estrato:  ')
        sexo = input('Masculino(M) O FEMENINO(F):  ').upper()
        fnt_agregar(mi_diccionario, id, nombre, apellidos, edad, estrato)
    if op == '2':
        print('cantidad de registrados: ', len(mi_diccionario)) 
        for clave, valor in mi_diccionario.items(): 
            print(f"{clave}:{valor}") 
        print('cantidad de pendientes: ', len(pendiente_lista))
        print(pendiente_lista)
        enter = input('Presione >ENTER< para continuar...') 
    if op == '3':
        sw= False
        
sw = True
while sw == True:
    opciones = input('\n\n>>>MENÚ<<<\n\n1. Registrar\n2. Mostrar\n3. Salir\n->')
    fnt_selector(opciones)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        