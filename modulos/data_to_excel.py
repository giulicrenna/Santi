import os, sys
import sqlite3
import pandas as pd
import openpyxl

def converter():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")

    db = sqlite3.connect(db_path)
    cur = db.cursor()

    data_ = cur.execute("SELECT dni,nombre,puntos_ciudadanos FROM ciudadanos")
    data = pd.DataFrame(data_, columns=['DNI','Nombre','Puntos Ciudadanos'])
    _data_ = data.sort_values('Puntos Ciudadanos',ascending=False)


    opcion = input('Pulse enter para convertir los resultados a un archivo Excel: ')
    if opcion == '':
        _data_.to_excel("resultados.xlsx",
             sheet_name='Resultados Santi') 
    else:
        _data_.to_excel("resultados.xlsx",
             sheet_name='Resultados Santi') 

converter()