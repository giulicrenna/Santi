# coding=utf8

import sqlite3
import os
import os.path
import sys
import pandas as pd

def ag():
    os.system('cls')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    
    #QUESTION CHAIN 

    dni = input('Escriba el DNI del individuo: ')
    nombre = input('Digite Nombre y apellido: ')
    edad = input('Digite edad de ' +nombre+ ': ')
    estudios_secundarios_bool = input('¿Tiene ' +nombre+ ' estudios secundarios?: ')
    if estudios_secundarios_bool == 'si':
        institucion_est_sec = input('¿Escribe el nombre de la institución: ')
    elif estudios_secundarios_bool == 'no':
        institucion_est_sec = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    estudios_de_grado_bool = input('¿Tiene ' +nombre+ ' estudios universitarios? ')
    if estudios_de_grado_bool == 'si':
        institucion_est_grado = input('Escriba la universidad en donde se graduó: ')
    elif estudios_de_grado_bool == 'no':
        institucion_est_grado = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    estudios_posgrado_bool =input('¿Tiene ' +nombre+ ' estudio de posgrado?: ')
    if estudios_posgrado_bool == 'si':
        institucion_est_pos = input('¿Escriba el nombre de la institución donde los cursó: ')
    elif estudios_posgrado_bool:
        institucion_est_pos = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    enfermedad_mental_bool = input('¿Tiene ' +nombre+ ' alguna enfermadad mental?: ')
    if enfermedad_mental_bool == 'si':
        enfermedad_mental = input('¿Cual?: ')
    elif enfermedad_mental_bool == 'no':
        enfermedad_mental = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    ejercito_bool = input('¿Estuvo ' +nombre+ ' en el ejercito Argentino?:')
    partido_politico_bool = input('¿Está ' +nombre+ ' en algun partido político?: ')
    if partido_politico_bool == 'si':
        partido_politico = input('¿Cual?: ')
    elif partido_politico_bool == 'no':
        partido_politico = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    cargos_penales_bool = input('¿Tiene ' +nombre+ ' cargos penales?: ')
    if cargos_penales_bool == 'si':
        cargos_penales_cant = input('¿Cuantos?: ')
    elif cargos_penales_bool:
        cargos_penales_cant = ''
    else:
        opcion = input('Incorrecto, pulsa Enter para volver: ')
        if opcion == '':
            ag()
    asesinatos_int = input('¿Ha ' +nombre+ ' asesinado a alguien?: ')
    puntos_ciudadanos = input('Escriba el PC de ' +nombre+ ': ')

    # Esepcificar en que columna de la tabla irá el valór
    cur.execute("insert or ignore into ciudadanos('dni','nombre','edad','estudios_secundarios_bool','institucion_est_sec','estudios_de_grado_bool','institucion_est_grado','estudios_posgrado_bool','institucion_est_pos','enfermedad_mental_bool','enfermedad_mental','ejercito_bool','partido_politico_bool','partido_politico','cargos_penales_bool','cargos_penales_cant','asesinatos_int','puntos_ciudadanos') values ('"+dni+"','"+nombre+"','"+edad+"','"+estudios_secundarios_bool+"','"+institucion_est_sec+"','"+estudios_de_grado_bool+"','"+institucion_est_grado+"','"+estudios_posgrado_bool+"','"+institucion_est_pos+"','"+enfermedad_mental_bool+"','"+enfermedad_mental+"','"+ejercito_bool+"','"+partido_politico_bool+"','"+partido_politico+"','"+cargos_penales_bool+"','"+cargos_penales_cant+"','"+asesinatos_int+"','"+puntos_ciudadanos+"')")
    db.commit()
    cur.close()
    os.system('cls')
    print('')
    print('         --------------------------------')
    print('         Ciudadano agregado exitosamente.')
    print('         --------------------------------')
    print('')
    print('---------------------------------------------------')
    print('-    [a] Agregar otra personas a la base de datos -')
    print('-                                                 -')
    print('-    [v] Ver info. personas                       -')
    print('-                                                 -')
    print('-    [m] Modificar info. personas                 -')
    print('-                                                 -')
    print('-    [e] Eliminar personas de la base de datos    -')
    print('-                                                 -')
    print('-    [s] Salir del programa                       -')
    print('---------------------------------------------------')
    print('')

    opcion = input('Digite una opción: ')

    if opcion == 'a':
        ag()
    elif opcion == 'v':    
        ver()
    elif opcion == 'm':
        mod()
    elif opcion == 'e':
        elim()
    elif opcion == 's':
        sys.exit()
    else:
        print('Seleción incorrecta, apriete enter para volver al menú:')
        opcion = input()
        if opcion == '':
            menu()

    opcion2 = input('Apriete enter para volver al menú: ')
    if opcion2 == '':
        menu()
    else:
        menu()
def ver():
    os.system('cls')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")
    db = sqlite3.connect(db_path)
    cur = db.cursor()

    cur.execute('SELECT * FROM ciudadanos')
    data = cur.fetchall()
    data_table = pd.DataFrame(data, columns=['id','dni','nombre','edad','Est. Sec','Sec','Est. Grado','Facultad','Est. Pos','Facultad','Enfermedad mental','Enfermedad mental','ejercito','part. político','part. político','Cargos penales','Cant.','Asesinatos','PC'])
    print(data_table)
    
                                    
    db.close

def mod():
    os.system('cls')

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))    
    db_path = os.path.join(BASE_DIR, "data_base.s3db")
    db = sqlite3.connect(db_path)
    c = db.cursor()

    id_ = input('Digite el DNI de la persona a modificar: ')
    os.system('cls')
    print('-------------------------------------------------')
    print('           ¿Que quieres modificar?')
    print('')
    print('\t1.  Nombre ')
    print('\t2.  Edad ')
    print('\t3.  Estudios Secundarios ')
    print('\t4.  Institución de estudios secundarios ')
    print('\t5.  Estudios de grado ')
    print('\t6.  Institución de estudios de grado')
    print('\t7.  Estudios de posgrado')
    print('\t8.  Institución de estudios de posgrado')
    print('\t9.  Enfermedad mental')
    print('\t10. nombre de enfermedad mental')
    print('\t11. Ejército ')
    print('\t12. partido Político')
    print('\t13. Nombre partido político')
    print('\t14. Cargos penales')
    print('\t15. cantidad de cargos penales')
    print('\t16. Asesinatos')
    print('\t17. Puntos Ciudadanos')

    opcion = input('Digite una opción: ')

    if opcion == '1':
        nuevo_valor = input('Escribe el nuevo nombre: ')
        c.execute("update ciudadanos set nombre =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '2':
        nuevo_valor = input('Escribe la nueva edad: ')
        c.execute("update ciudadanos set edad =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '3':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set estudios_secundarios_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set estudios_secundarios_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '4':
        nuevo_valor = input('Escriba el nombre del nuevo valor: ')
        c.execute("update ciudadanos set institucion_est_sec =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '5':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set estudios_de_grado_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set estudios_de_grado_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '6':
        nuevo_valor = input('Escriba el nombre del nuevo valor: ')
        c.execute("update ciudadanos set institucion_est_grado =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '7':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set estudios_posgrado_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set estudios_posgrado_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '8':
        nuevo_valor = input('Escriba el nombre del nuevo valor: ')
        c.execute("update ciudadanos set institucion_est_pos =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '9':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set enfermedad_mental_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set enfermedad_mental_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '10':
        nuevo_valor = input('Escriba el nombre de la enfermedad mental: ')
        c.execute("update ciudadanos set enfermedad_mental =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '11':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set ejercito_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set ejercito_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '12':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set partido_politico_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set partido_politico_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '13':
        nuevo_valor = input('Escriba el nombre del nuevo partido político: ')
        c.execute("update ciudadanos set partido_politico =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '14':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set cargos_penales_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set cargos_penales_bool =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '15':
        nuevo_valor = input('Escriba la nueva cantidad: ')
        c.execute("update ciudadanos set cargos_penales_cant =('"+nuevo_valor+"') where dni = ('"+id_+"')")
    elif opcion == '16':
        nuevo_valor = input('Escribe el nuevo valor (si o no): ')
        if nuevo_valor == 'si':
            c.execute("update ciudadanos set asesinatos_int =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        elif nuevo_valor == 'no':
            c.execute("update ciudadanos set asesinatos_int =('"+nuevo_valor+"') where dni = ('"+id_+"')")
        else:
            opcion = input('Valor incorrento, apriete enter para volver: ')
            if opcion == '':    
                mod()
    elif opcion == '17':
        nuevo_valor = input('Digite el nuevo PC: ')
        c.execute("update ciudadanos set puntos_ciudadanos =('"+nuevo_valor+"') where dni = ('"+id_+"')")      
        if nuevo_valor == str:
            mod()
    else:
        opcion2 = input('Opción incorrecta, apriete enter para volver a modificar: ')
        if opcion2 == '':
            mod()
        else:
            mod()

    db.commit()
    c.close()


    os.system('cls')
    print('')
    print('        --------------------------------')
    print('        Ciudadano agregado exitosamente.')
    print('        --------------------------------')
    print('')
    print('---------------------------------------------------')
    print('-    [a] Agregar personas a la base de datos      -')
    print('-                                                 -')
    print('-    [v] Ver info. personas                       -')
    print('-                                                 -')
    print('-    [m] Modificar otra persona                   -')
    print('-                                                 -')
    print('-    [e] Eliminar personas de la base de datos    -')
    print('-                                                 -')
    print('-    [s] Salir del programa                       -')
    print('---------------------------------------------------')
    print('')

    opcion = input('Digite una opción: ')

    if opcion == 'a':
        ag()
    elif opcion == 'v':    
        ver()
    elif opcion == 'm':
        mod()
    elif opcion == 'e':
        elim()
    elif opcion == 's':
        sys.exit()
    else:
        print('Seleción incorrecta, apriete enter para volver al menú:')
        opcion = input()
        if opcion == '':
            menu()

def elim():
    os.system('cls')
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")
    db = sqlite3.connect(db_path)
    cur = db.cursor()
 
    id_ = input('Inserte el DNI de la persona a eliminar de la base de datos: ')
    cur.execute("DELETE  from ciudadanos where dni = ('"+id_+"')")

    db.commit()
    db.close()
    os.system('cls')

    print('')
    print('        --------------------------------')
    print('        Ciudadano agregado exitosamente.')
    print('        --------------------------------')
    print('')
    print('----------------------------------------------------')
    print('-    [a] Agregar personas a la base de datos       -')
    print('-                                                  -')
    print('-    [v] Ver info. personas                        -')
    print('-                                                  -')
    print('-    [m] Modificar info. de persona                -')
    print('-                                                  -')
    print('-    [e] Eliminar otra persona de la base de datos -')
    print('-                                                  -')
    print('-    [s] Salir del programa                        -')
    print('----------------------------------------------------')
    print('')

    opcion = input('Digite una opción: ')

    if opcion == 'a':
        ag()
    elif opcion == 'v':    
        ver()
    elif opcion == 'm':
        mod()
    elif opcion == 'e':
        elim()
    elif opcion == 's':
        sys.exit()
    else:
        print('Seleción incorrecta, apriete enter para volver al menú:')
        opcion = input()
        if opcion == '':
            menu()

def menu():
    os.system('cls')

    print('')
    print('BASE DE DATOS CIUDADANOS DE LA REPÚBLICA ARGENTINA')
    print('')
    print('                   _SANTI_                        ')
    print('')
    print('')
    print('')    
    print('-------------------------------------------------')
    print('-    [a] Agregar personas a la base de datos    -')
    print('-                                               -')
    print('-    [v] Ver info. personas                     -')
    print('-                                               -')
    print('-    [m] Modificar info. personas               -')
    print('-                                               -')
    print('-    [e] Eliminar personas de la base de datos  -')
    print('-                                               -')
    print('-    [s] Salir del programa                     -')
    print('-------------------------------------------------')
    print('')

    opcion = input('Digite una opción: ')

    if opcion == 'a':
        ag()
    elif opcion == 'v':    
        ver()
    elif opcion == 'm':
        mod()
    elif opcion == 'e':
        elim()
    elif opcion == 's':
        sys.exit()
    else:
        print('Seleción incorrecta, apriete enter para volver al menú:')
        opcion = input()
        if opcion == '':
            menu()
menu()