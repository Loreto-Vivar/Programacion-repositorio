from collections import Counter
import re

def contar_palabras(texto):
    #Convertir a minúsculas y eliminar caracteres no alfabéticos
    palabras = re.findall(r'\b\w+\b', texto.lower())
    #Contar la frecuencia de cada palabra
    frecuencia = Counter(palabras)
    return frecuencia

texto = input("Ingrese un texto: ")
resultado = contar_palabras(texto)
print("Frecuencia de palabras:",resultado)