#program.py

sum = 1 + 2 # 3
product = sum * 2
print("El resultado es: ", product)

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())
print("La fecha de hoy es: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print("El resultado es:", int(first_number) + int(second_number))