import os
import sqlite3
import glob
from os.path import basename, splitext
import os.path
import sys

from PyQt5.QtWidgets import QMessageBox
if not os.path.exists("databases"):
    os.makedirs("databases")

def tables_dif(*db_names):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    res = {}
    for db_name in db_names:
        con.execute("ATTACH DATABASE './databases/%s' AS db" % db_name)
        #SELECT  * FROM db.formateur,db.formation as t2 LEFT JOIN db.formateur ON db.formateur.id = db.formation.id
        sql ='''
                SELECT  * FROM db.formateur,db.formation where db.formateur.id = db.formation.id
             '''
        cur.execute(sql)
        res[db_name] = cur.fetchall()

        print("xxxxxxxxxxxxxxxx",res[db_name])
        for x in res[db_name]:
            print("zzzzzzzzzzzzz", x[0])
            # if (x[3]=="user"):
            #      print("Naissance",x[0])

        con.execute("DETACH DATABASE db")
    con.close()
    return res
# Recuperation du nom du base de donnee total
fichier_total = (glob.glob('*.ESD'))

# Recuperation du nom du base de donnee brute
fichier_brute = glob.glob('databases//*.db')
repertoire_fichier_brute = os.listdir('databases//')
print("MMMMMMMMMM",fichier_brute)
print("NNNNNNNN",repertoire_fichier_brute)

def compar():

    for fichier_brute_bdd in repertoire_fichier_brute:
        extension = os.path.splitext(fichier_brute_bdd)
        print("RRRRR",extension[1])
        if (".db" in extension[1]):
            print(tables_dif('{}'.format(fichier_brute_bdd)))
            print("Vita ny traitement")

