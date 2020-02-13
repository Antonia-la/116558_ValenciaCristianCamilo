#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:03:42 2020

@author: cristian
"""
'Cristian camilo valencia /116558'


#Punto 1
print('VALOR ABSOLUTO')
punto1= float(input('Escriba un numero:'))
if punto1 <0:
    resultado= punto1 * -1
    print('El valor absoluto de', punto1,'es:', resultado)
    
else:
    print('El valor absoluto de', punto1, 'es:', punto1)
   
 

#%% punto 2.
#Leer dos números enteros y determinar si la magnitud de la diferencia entre 
#los dos es un número primo.

import math
numero = float(input('favor ingresar un numero = '))
numero2 = float(input('favor ingresar un numero = '))
dif=numero - numero2
dif= int(math.sqrt(dif*dif))
print(dif)
contador = 0
for i in range(1,dif+1):
    if (dif% i)==0:
        contador = contador + 1

if contador==2:
    print("el numero es primo")
else:
    print("el numero no es primo")  
        
#%%
#Punto3
# iterar a través de los primeros cien enteros positivos, 
#buscando los múltiplos de 3 e imprimiendo y almacenándolos en
#una lista hasta encontrar los primeros 15 de ellos. Una vez encontrados, 
#continuar iterando en busca de los múltiplos de 4 y almacenarlos en otra lista


def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 
# lista que contendra los valores multiples
multiples_3=[]
multiples_4=[]
 
# bucle del 1 al 100
for i in range(1,101):
 
    if multiple(i,3) and len(multiples_3)<16:
        multiples_3.append(i)
        x =i

for j in range(x,101):
    if multiple(j,4):
        multiples_4.append(j)
    
 
print ("Los multiples de 3 son: " , multiples_3)

print ("Los multiples de 4 son: ", multiples_4)
        

#%% Punto4. Hacer un programa que lea las coordenadas (x1,y1,r1) y (x2,y2,r2) 
#Lea coordenadas las (a,b), determinar si (a,b) está contenido 
#en el  círculo 1
#en el círculo 2 
#dentro de ambos 
#fuera de ambos 

import math as math 
       
p= eval(input('Digite las coordenadas (a,b):'))
a= p[0]
b= p[1]
#Se aclara que el circulo 1 es el más grande, el circulo 2 es el interno.
x1=0
x2=0
y1=0
y2=0
r1 = 10
r2 = 5

distancia= math.sqrt((x2-a)**2+(x2-b)**2)

if 5<distancia<10 :
    print(p, 'Esta contenido en el circulo 1')
    
elif distancia <= r2:
    print(p, 'Esta contenido en el circulo 1 y 2')

elif distancia > r2:
    print(p, 'Esta fuera del circulo 1 y del circulo 2')
    
#%%
#Punto 5

def comprobacion():
    palabra = str(input("ingrese una palabra: "))
    vocales = "aeiou"
    tildes = "áéíóúÁÉÍÓÚ"
    contador = 0
    espacio = 0
    print("ingresaron este numero de vocales de esta palabra", palabra)
    for v in vocales:
        print(v, palabra.lower().count(v))

    print("Se ingresaron estas letras con tildes")
    for v in tildes:
        "print(v, palabra.lower().count(v))"#ver detalladamente
        if(v == "á"  and v == "é" and v == "í" and v == "ó" and v == "ú" and \
           v == "Á"  and v == "É" and v == "Í" and v == "Ó" and v == "Ú"):
            contador = contador+1
    print(contador)

    print("Cuantos digitos entraron:")
    for v in palabra:
        contador = contador + 1
    print("Entraron ",contador," digitos")

    print("Cuantos espacios entraron:")
    for v in palabra:
        if(v == '' or v == " "):
            espacio = espacio+1
    print("Entraron ",espacio, 'espacios')

    print('cuántas palabras reservadas se entraron:')
    countpalabra = 0;
    PalabrasReservadas = ["and","except","lambda","with","as","finally",
                          "nonlocal","while","assert","false","None","yield",
                          "break","for","not","class","from","or","continue",
                          "global","pass","def","if","raise","del","import",
                          "return","elif","in","True","else","is","try"]
    for i in PalabrasReservadas:
        if (palabra == i):
            countpalabra = countpalabra+1

    print("Entraron ", countpalabra, 'palabras reservadas')

#%% CADENAS
#punto5.Escribir un programa que reciba una cadena de texto y reporte
#a) cuántas letras vocales en mayúscula se entraron;
#b) cuántas letras con tilde se entraron (minúsculas y mayúsculas);
#c) cuántos dígitos se entraron, 
#d) cuántos espacios se entraron;
#e) cuántas palabras reservadas se entraron.
import keyword
texto= input("escriba una palabra")
M="AEIOUÁÉÍÓÚ"
S1=[]
for i in range(0, len(texto)):
   if texto[i] in M:
       S1.append(texto[i])
print ("tiene", len(S1),"vocales mayusculas")

MT="ÁÉÍÓÚáéíóú"
S2=[]
for i in range(0, len(texto)):
   if texto[i] in MT:
       S2.append(texto[i])
print ("tiene", len(S2),"vocales con tilde")

num="0123456789"
S3=[]
for i in range(0, len(texto)):
   if texto[i] in num:
       S3.append(texto[i])
print ("tiene", len(S3),"digitos")


espacio= " "
S4=[]
for i in range(0, len(texto)):
   if texto[i] in espacio:
       S4.append(texto[i])
print ("tiene", len(S4),"espacios")

S5=texto.split()
S6=[]
for i in range(0, len(S5)):
   if [i] in keyword.kwlist:
       S6.append(S5[i])
print (S6,"son keywords contenidas en la palabra digitada")





#%% Punto 6.
#Leer una cadena de texto y organizar alfabéticamente cada una de las 
#letras que la componen, repitiendo cada una tantas veces como se encuentra. 
#Por ejemplo, la cadena ‘tarea importante’ será ‘aaaeeimnoprrttt’. 
#(Note que no se incluyen los espacios).

print("digite la cadena")
cadena=input()
cadena=cadena.replace(' ', '')
lista=[]
for i in cadena:
    lista.append(i)
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
print(cadena2)


#%%
#Punto 7
#Leer una lista de números ya ordenados de forma ascendente y verificar que 
#dicha lista está ordenada. Luego, leer un número e insertarlo en la lista 
#en la posición que le corresponde a dicho número.
   
def nuevoNumero():
    listaNumeros = [1,2,6,5,6,7,9,10]
    print(listaNumeros)
    numero = int(input("ingrese un nuevo numero: "))
    listaNumeros.append(numero)
    x = sorted(listaNumeros)
    print(x)
    



    

#%% punto8.
# Leer una lista de números enteros y determinar cual es el segundo 
#elemento mayor de dicha lista. No utilizar ningún tipo de algoritmo de 
#ordenamiento para realizar este ejercicio. Por ejemplo, en la 
#lista [11, 22, 3, 4, 22], el segundo número mayor sería el 11; de otro lado, 
#en la lista [1, 1, 1, 1, 1] no existe un segundo elemento mayor.
   
    
def segundoMayor():
    list1 = eval(input('Digite por favor una lista:'))
    listanueva= []
    m = max(list1)
    for u in range(len(list1)):
        if list1[u] < m:
            listanueva.append(list1[u])

    print(max(listanueva))
        
        
#%%
#Punto 9
## 9.Escribir un programa que calcule términos de la sucesión 
#Un+1 = 3 Un + 1 si Un es impar y U n+1 = Un / 2 si Un es par. 
#El programa tiene que pedir el término U0 y el número de términos a calcular

punto9 = int(input('Digame el valor de U(O):'))

magnitud = int(input('Digame cuántos términos quiere:'))

lista9= [punto9]

for i in range(magnitud-1):
    if punto9 % 2 == 0:
        punto9 = int(punto9/2)
        lista9.append(punto9)  
        
    else:
        punto9 = int(punto9*3 +1)
        lista9.append(punto9) 
        
print(lista9)
      
#%% Punto10. 
#Leer una matriz e imprimir el vector que aparece cuando la matriz 
#se desenreda en forma de espiral que gira en el sentido horario a partir de 
#la esquina inferior derecha
   
import random
n = int(5)
matriz=[None]*n
for i in range(0,n):
    matriz[i] = [None]*n
for i in range(0,n):
    for j in range(0,n):
        matriz[i][j] = (int)(random.randint(1,1001))
print(matriz)
for i in range(n-1,-1,-1):
    if(i%2==0):
        for j in range(n-1,-1,-1):
            print (matriz[j][i])
    else:
        for j in range(0,n):
            print (matriz[j][i])
            
            
#%% Punto11. 
#Diseñar una función de tres parámetros que pida la altura y anchura 
#de un rectángulo, y el carácter a utilizar para dibujarlo.

def rectangulo(ancho, alto, letra):
    for i in range(alto):
        for j in range(ancho):
            print(letra, end=" ")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = input("Carácter a utilizar: ")
rectangulo(anchura, altura, caracter)  


#%% Punto 12
#Diseñar una función que pida la anchura de un triángulo y lo dibuje con 
#caracteres producto (*).
        
def triángulo():

    anchura = int(input("Anchura del triángulo: "))
    
    for i in range(1, anchura + 1):
        for j in range(i):
            print("* ", end="")
        print()
    
    for i in range(1, anchura):
        for j in range(anchura - i):
            print("* ", end="")
        print()
        
#%%
#Punto 13
# Diseñar una función que pida dos años y escriba cuántos años bisiestos 
#hay entre esas dos fechas (incluidos los dos años).
def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Contador de años bisiestos")
inicio = int(input("Escriba un año: "))
print("Escriba otro año posterior a", str(inicio) + ": ", end="")
final = int(input())
while final < inicio:
    print(final, "no es mayor que", str(inicio) + ". Inténtelo de nuevo: ",
          end="")
    final = int(input())

contador = 0
for i in range(inicio, final + 1):
    if es_bisiesto(i):
        contador += 1

print("De", inicio, "a", final, "hay", final - inicio + 1, "años,",
      contador, "de ellos bisiestos.")

#%%
#Punto 14
# 14. Diseñar una función que proponga sumas de números positivos 
#(dos números entre 1 y 100) al usuario y compruebe la respuesta. 
#El programa continuará hasta que se acierten cinco sumas. 
#(Tip: para generar los números enteros aleatorios, 
#existe la función random.randint(a,b) de la librería random).

def sumas():
    import random as rd
    
    print('Escriba el resultado de las siguientes operaciones:')
    
    n= 0
    
    while n!=5:
        a= rd.randint(0,100)
        b= rd.randint(0,100)
    
        rusuario= int(input(f'{a}+{b}='))
        
        resultado= a+b
        
        if (rusuario==resultado):
            n+=1
            print('¡RESPUESTA CORRECTA!')
            
        elif(rusuario!=resultado):
            print('¡RESULTADO INCORRECTO!')
            
    
    print('Programa Terminado')

#%%
#Punto 15

import random as rd

   
def mastermind():
    long = int(input('Digite la longitud de la cadena entre (2 a 9) cifras:'))
    cadena = ''
    
    if(long >= 2 and long <= 9 ):
        for i in range(long):
            aleatorio = rd.randint(0,9)
            cadena += str(aleatorio)
        print(cadena)

        intentos = input('Por favor adivine la cadena:')
        c = intentos
        acumulador = 1
        while c != cadena:
            print('Se ha equivocado, vuelva a intentarlo')

            intentos = input('Por favor adivine la cadena:')
            v = 0
            acumulador = acumulador+1
            if(acumulador == 15):
                print("Has perdido 15 veces  ");
                print("PERDISTES EL JUEGO  ")
                break;

            print("Intento numero: ", acumulador)
            for z in range(0, len(cadena)):

                if cadena[z] == intentos[z]:
                    v += 1

            print('Ha adivinado', v, 'digitos')
            if(long == v):
                print("Has acertado a toda la cadena")
                print("GANASTE")
                break;
    else:
        print("Por favor inserte la cadena que este rango (2 a 9)")
        print("intente insertar de nuevo el valor ")

mastermind();










                                                                                                                                                                                                                                               