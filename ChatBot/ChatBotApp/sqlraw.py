import sqlite3
import os
import pandas
iris=pandas.read_csv('iris.csv')
print(iris.head())

def pobieranko(iris):
    lista=[]
    if os.path.isfile('iris.csv'):
        with open('iris.csv', "r") as dane:
            for rows in dane:
                #rows=rows.decode("utf-8")
                lista.append(tuple(rows.split(",")))
            return tuple(lista)
print(pobieranko(iris))
#connection=sqlite3.connect('iris.csv')
print('ddd')
