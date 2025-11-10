import math

numeros = input("Introduce una lista de números separados por comas: ")
numeros = [float(n) for n in numeros.split(",")]

media = sum(numeros) / len(numeros)
desviacion = math.sqrt(sum((x - media) ** 2 for x in numeros) / len(numeros))

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")
