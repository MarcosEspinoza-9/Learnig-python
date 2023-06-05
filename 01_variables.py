#VARIABLES
MyVariable = "My String variable"
print(MyVariable) 

print(len(MyVariable))  #len devuelve la longuitud de variable

#CONCATENACIÓN
print("hola mundo:" , MyVariable)

#VARIABLES EN UNA SOLA LINEA ASIGNANDO VALORES PREDETERMINADOS
nombre , apellido = "Marcos" , "Espinoza"
print(nombre , apellido)

#INGRESAR DATOS CON UN INPUT  
primer_Nombre = input("Cual es tu primer nombre?")
edad = input("Cual es tuEdad?")

print("Tu nombre es:" , primer_Nombre, "y tienes:" , edad)

#forzamos el tipado
address: str = "2 de abril"
address = True
address = 5
address = 1.2
print(type(address))

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']