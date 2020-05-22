import os, sys



print('')
print('------------------------SANTI------------------')
print('')
print('                         MENÚ                  ')
print('')
print('')
print('')    
print('-------------------------------------------------')
print('-    [1] Abrir algoritmo                        -')
print('-                                               -')
print('-    [2] Abrir Base de datos                    -')
print('-                                               -')
print('-    [3] Abrir controlador de base de datos     -')
print('-                                               -')
print('-    [4] Restaurar Puntos Ciudadanos            -')
print('-                                               -')
print('-    [5] Importar resultados a archivo excel    -')
print('-------------------------------------------------')
print('')
print('')

opcion = input('Digite su opción: ')

if opcion == '1':
    from modulos import santi
elif opcion == '2':
    print('hola')
elif opcion == '3':
    from modulos import driver_base_de_datos
elif opcion == '4':
    from modulos import eraser
elif opcion == '5':
    from modulos import data_to_excel
    
