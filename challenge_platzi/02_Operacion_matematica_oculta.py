
# 02. **Operación Matemática Oculta**
'''
Encuentra la lógica de las siguientes operaciones y números:
* 5 + 4 = 19
* 8 + 2 = 610
* 10 + 8 = 218
* 12 + 9 = 321
* 18 + 2 = 1620
* 21 + 5 = 1626
'''
# Desarrolo
'''
Por pura observación podemos ver que los primeros digitos corresponden a una resta del primer elemento y segundo elemento,
este resultado se encuentra concatenado al resultado de la suma de los mismo elementos
'''

def op_math (num1,num2):
     resta = num1 - num2
     suma = num1 + num2
     resultado = int(str(resta) + str(suma))
     return resultado

#Confirmamos nuestra hipotesis

print(f'5 + 4 = {op_math(5,4)}')
print(f'8 + 2 = {op_math(8,2)}')
print(f'10 + 8 = {op_math(10,8)}')
print(f'12 + 9 = {op_math(12,9)}')
print(f'18 + 2 = {op_math(18,2)}')
print(f'21 + 5 = {op_math(21,5)}')