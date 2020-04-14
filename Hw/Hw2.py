# Tarea 2
# Crear un pequeño sistemita de ventas de fruta
# Lista de frutas
# menu
# Agregar una fruta
# Ver si la fruta esta disponible
# Eliminar frutar

list_frutas = []
Tienda = ['Mango', 'Chirimoya', 'Manzana', 'Papaya']
sw = True
while sw is True:
    print('''
    ********************************
                TIENDA
    1. Agregar una fruta al carrito(Comprar)
    2. Revisar fruta disponible
    3. Eliminar fruta
    4. Mostrar compra
    5. Salir
    ''')
    case = int(input('Ingrese opcion: '))
    if case is 1:
        cad = input('Fruta a comprar: ')
        list_frutas.append(cad)
        print(cad, 'agregada correctamente')
    elif case is 2:
        cad = input('Fruta a buscar: ')
        sw2 = False
        for fruta in Tienda:
            if fruta is cad:
                sw2 = True
        if sw2 is True:
            print(cad, 'si existe en la Tienda')
        else:
            print(cad, 'no existe en la Tienda')
    elif case is 3:
        cad = input('Fruta a eliminar: ')
        sw2 = False
        for fruta in Tienda:
            if fruta == cad:
                sw2 = True
        if sw2 is True:
            list_frutas.remove(cad)
            print(cad, 'eliminado')
        else:
            print('No se encontre para eliminar')
    elif case is 4:
        print('\tLista de compra')
        for fruta in list_frutas:
            print('\t- ', fruta)
    elif case is 5:
        print('Compra finalizada')
        sw = False
    else:
        print(f'La opción {case} no disponible')
