# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import sys   
entrada=raw_input("ingrese los datos de entrada: ")
entrada=entrada.split(" ")

while (len(entrada)>4):
        print("Los Datos no se ingresaron correctamente\n")
        entrada=raw_input("ingrese los datos de entrada: ")
        entrada=entrada.split(" ") 
contador=0
while contador<4:
    entrada[contador]=int(entrada[contador])
    contador+=1
while (entrada[0]-1<entrada[3]):
        print("Los Datos no se ingresaron correctamente\n")
        entrada=raw_input("ingrese los datos de entrada: ")
        entrada=entrada.split(" ")  
contador=0        
while contador<4:
    entrada[contador]=int(entrada[contador])
    contador+=1        
grafo=[]
contador=0
while contador<=entrada[0]:
        m=[]
        contador1=0
        while contador1<= entrada[0]:
            m.append(0)
            contador1+=1
        grafo.append(m)
        contador+=1
n=entrada[0]+1
b=entrada[1]
f=entrada[2]
cross=entrada[3]
ultima=cross+2

nodos=2
#agrega las ramas correspondientes
while cross>=0:
    grafo[0][nodos-1]=1
   
    if b>0:#genera el camino de vuelta al padre
        grafo[nodos-1][0]=1
        b-=1
    nodos+=1
    
    cross-=1
#agrega nodos hijos 
mas=1
r=entrada[3]+2

while nodos<=n:
 

    
    if f>0:
        grafo[0][r]=1
        r+=1
        f-=1
    elif f>0 and mas<entrada[3]+1 :
        grafo[mas][ultima+entrada[3]+1]=1
        f-=1
   
    grafo[mas][ultima]=1
  
    if b>0:#genera el camino al padre 
        grafo[ultima][mas]=1
        b-=1
    mas+=1    
    ultima+=1
    nodos+=1
#condicion cuando faltan forward
if f>0 or b>0:
    print "La combinacion de numeros no es factible"
    raw_input()
    sys.exit()

    
#genera el registro de el cross del trayecto de stack


contador2=1

    
while grafo[0][contador2]==1 and contador2<len(grafo[0])-1 and contador2<entrada[3]+1:
        
        if grafo[0][contador2]==1 and grafo[0][contador2+1]==1:
            grafo[contador2+1][contador2]=1
            contador2+=1
        else:
            contador2+=1

        

#//////////////////////////////////////////
#imprimir grafo
for i in grafo:
    print i
print n
indice=1
for i in grafo:
    palabra=""
    palabra+=str(i.count(1))
    palabra+=" "
    contador=0
    while contador<len(i):
        if i[contador]==1:
            palabra+=str(contador+1)
            palabra+=" "
            contador+=1
        else:
            contador+=1
            
    print indice,".-",palabra  
    indice+=1
raw_input("")       
    