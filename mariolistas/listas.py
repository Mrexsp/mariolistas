'''
Created on 20 dic. 2016

@author: usuario
'''
from Listas.Deflistas import CrearLista
from Listas.Deflistas import Subs
from Listas.Deflistas import mayor
from Listas.Deflistas import menor
from Listas.Deflistas import comas
l=[]
CrearLista(l)
print (l)
while True:
    sino=input("¿Quiere añadir algo más?")
    if sino=="Sí" or sino=="si" or sino=="Si" or sino=="sí" or sino=="":
        CrearLista(l)
        print (l)
    else:
        break

id_paciente, fase_ensayo, serie_temperaturas=Subs(l)
for posicion in range(len(serie_temperaturas)):
    serie_temperaturas[posicion] = float(serie_temperaturas[posicion])
ium=int(len(l)-2)
mayor(serie_temperaturas)
menor(serie_temperaturas)
comas(serie_temperaturas)
print ("Tenemos el siguiente número de temperaturas: %i" %ium)
print ("El mayor es: %i" %mayor(serie_temperaturas))
print ("El menor es: %i" %menor(serie_temperaturas))
