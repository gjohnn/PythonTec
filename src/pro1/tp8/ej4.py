'''      
    4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
	1 es impar.
	Si un número es impar, su antecesor es par; y viceversa.
 '''
 
from functions import even


n = int(input("Ingrese n: "))

even(n)