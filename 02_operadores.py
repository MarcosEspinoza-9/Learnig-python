# OPERADORES ARITMETICOS

print('Estos es una suma: ', 1 + 2)     
print('Estos es una resta: ', 1 - 2)     
print('Estos es una multiplicacion: ', 1 * 2)     
print('Estos es una divicion: ', 1 / 2)     
print('Estos es un residuo: ', 5 % 15)     
print('Estos es al cuadrado : ', 1 ** 987)     

#print("hola Mundo " + str(5))

print("****OPERADORES COMPARATIVOS****")
## OPERADOR COMPARATIVO
print(3<4)
print(3>4)
print(4<=4)
print(4>=4)
print(1==4)
print(3 > 2 and 4 > 3)  # Se utiliza operador AND
print(3 > 2 or 4 > 3)  # Se utiliza operador OR
print (not 3 < 2 and 4 < 3)  # Se utiliza operador AND

print("OPERACIONES YA CON VALORES ALMACENADOS EN VARIABLES")
a = 3 
b = 12

print(a+b)
print(a-b)
print(a*b)


print("*** AREA DE UN CIRCULO ***")
radio = 18
PI = 3.1416
radio_circulo = PI * radio**2
print(radio_circulo)

""" 
Escriba un script que solicite al usuario que
ingrese la base y la altura del triángulo y calcule
el área de este triángulo (área = 0,5 xbxh).
"""

base = float(input("Escribe una base: "))
altura = float(input("Escribe una altura: "))

AreaTriangulo =  (base * altura) / 2
print("El area del triangulo es:", (AreaTriangulo)) 

