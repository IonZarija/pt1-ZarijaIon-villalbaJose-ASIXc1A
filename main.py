"""

"""
import random

def caracteres(palabra):
    cen = list(palabra[1:-2])
    random.shuffle(cen)
    return palabra[0] + ''.join(cen) + palabra[-2] + palabra[-1]

def desordPal(palabra):
   if len(palabra) <= 2:
       return palabra
   elif palabra[-1] == "," or "." or "!" or "?":
       return caracteres(palabra)
   else:
       cen = list(palabra[1:-1])
       random.shuffle(cen)
       return palabra[0] + ''.join(cen) + palabra[-1]

def dividirFrase(frase):
   palabras = frase.split()
   palDesord = [desordPal(palabra) for palabra in palabras]
   return ' '.join(palDesord)


frase = input("Introduce una frase: ")
fraseDesord = dividirFrase(frase)


print("Frase original:", frase)
print("Frase desordenada:", fraseDesord)