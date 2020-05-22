import os, sys
import sqlite3
import pandas as pd

def eraser():    # ----------------------------SCRIPT PARA RESTARURAR PUNTOS CIUDADANOS --------------------------------------
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "data_base.s3db")

    db = sqlite3.connect(db_path)
    cur = db.cursor()
    def erase(): 
        i = 0
        j = 1
        while i <= 100:              
            cur.execute("UPDATE ciudadanos SET puntos_ciudadanos = 0 WHERE id_db = ("+str(j)+")")                   
            i += 1
            j += 1                    
    erase()  
    db.commit()
    cur.close()
eraser()