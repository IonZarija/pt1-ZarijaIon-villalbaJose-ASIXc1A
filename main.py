"""

"""
import random


def desordenar_palabra(palabra):
   if len(palabra) <= 2:
       return palabra
   else:
       cen = list(palabra[1:-1])
       random.shuffle(cen)
       return palabra[0] + ''.join(cen) + palabra[-1]


def dividirFrase(frase):
   palabras = frase.split()
   palDesord = [desordenar_palabra(palabra) for palabra in palabras]
   return ' '.join(palDesord)


frase = input("Introduce una frase: ")
frase_desord = dividirFrase(frase)


print("Frase original:", frase)
print("Frase desordenada:", frase_desordenada)