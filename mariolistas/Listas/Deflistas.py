'''
Created on 9 dic. 2016

@author: usuario
'''
def CrearLista(lista):
    lis=input("Escriba para añadir algo a la lista.")
    lista.append(lis)
    return lis
def Subs(l):
    id_paciente = l[0]
    fase_ensayo = l[1]
    serie_temperaturas = l[2:]
    return id_paciente, fase_ensayo, serie_temperaturas
def mayor(serie_temperaturas): 
    mayor = serie_temperaturas[0] 
    for num in serie_temperaturas: 
        if num > mayor: 
            mayor = num 
    return mayor 
def menor(serie_temperaturas): 
    menor = serie_temperaturas[0] 
    for num in serie_temperaturas: 
        if num < menor: 
            menor = num 
    return menor 
def comas(serie_temperaturas):
    str(serie_temperaturas)
    print (serie_temperaturas)