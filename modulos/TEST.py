# TEST

import os, sys
import sqlite3
import pandas as pd

def con():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")

    db = sqlite3.connect(db_path)
    cur = db.cursor()
    cr = cur.execute("SELECT * FROM ciudadanos")
    data_ = cur.fetchall()
  
    data = pd.DataFrame(data_, columns=['id','dni','nombre','edad','secundarios','etc','grado','etc','pos','etc','enfermedad','etc','ejercito',
                        'partido','etc','penales','penales_cant','asesinatos','pc'])
    edad = data['edad']
    sec = data['secundarios']
    grado = data['grado']
    pos = data['pos']
    enf = data['enfermedad']
    ejercito = data['ejercito']
    part = data['partido']
    penales = data['penales']
    penales_cant = data['penales_cant']
    asesinatos = data['asesinatos']


    def santi(): #SANTI : SISTEMA DE ANALISIS NATURAL TOTALMENTE INFORMÁTICO 
        i = 0
        j = 1
        while i <= 3:              
            #---------------Parámetro 0-----------------------------------------------------
            if '17' >= str(edad[i]):
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 1000 WHERE id = ("+str(j)+")")             
            elif '18' <= str(edad[i]):
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 20 WHERE id = ("+str(j)+")")
            elif '80' >= str(edad[i]):
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 1000 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 1-----------------------------------------------------
            if sec[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 50 WHERE id = ("+str(j)+")")
            elif sec[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 100 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 2-----------------------------------------------------
            if grado[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 100 WHERE id = ("+str(j)+")")
            elif grado[i]  == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 50 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 3-----------------------------------------------------
            if pos[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 200 WHERE id = ("+str(j)+")")
            elif pos[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 10 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 4-----------------------------------------------------
            if enf[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 1000 WHERE id = ("+str(j)+")")
            elif enf[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 20 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 5-----------------------------------------------------
            if ejercito[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 150 WHERE id = ("+str(j)+")")
            elif ejercito[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 20 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 6-----------------------------------------------------
            if part[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 200 WHERE id = ("+str(j)+")")
            elif part[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 50 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 7-----------------------------------------------------
            if penales[i] == 'si':
                if penales_cant[i] >= 2:
                    cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 500 WHERE id = ("+str(j)+")")
                elif penales_cant[i] <= 1:
                    cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 250 WHERE id = ("+str(j)+")")
                else:
                    cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            elif penales[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 50 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            #---------------Parámetro 7-----------------------------------------------------
            if asesinatos[i] == 'si':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos - 5000 WHERE id = ("+str(j)+")")
            elif asesinatos[i] == 'no':
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 50 WHERE id = ("+str(j)+")")
            else:
                cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = puntos_ciudadanos + 0 WHERE id = ("+str(j)+")")
            i += 1
            j += 1     

    santi()
    db.commit()
    cur.close()
con()

def res():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")

    db = sqlite3.connect(db_path)
    cur = db.cursor()
    cr = cur.execute("SELECT * FROM ciudadanos")
    data_ = cur.execute("SELECT dni,nombre,puntos_ciudadanos FROM ciudadanos")
  
    data = pd.DataFrame(data_, columns=['DNI','Nombre','Puntos Ciudadanos'])
    _data_ = data.sort_values('Puntos Ciudadanos',ascending=False)

    opcion = input('Pulsa enter para mostrar resultados: ')
    if opcion == '':
        print(_data_)
    else:
        print(_data_)
res()

opcion2 = input('Pulsa enter para salir del programa: ')
if opcion2 == '':
    sys.exit()
else:
    sys.exit()