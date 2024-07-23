# 04. **Identifica la operación**
"""
Encuentra la lógica en las siguientes operaciones y números:

3 = 27
4 = 36
5 = 45
6 = 54
7 = 63
8 = 72
9 = ??
"""

## Desarrollo
"""
Tratando de buscar una relacion entre cada parte de la igualdad, se puede razonar como "que operacion debo realizar en el lado izquierdo para obtener el numero del lado derecho".
* En el primer ejemplo al 3 aplicando que operación me da 27, multiplicarlo por 9.
* Nos damos cuenta que se confirma para cada caso.
"""
## Solucion
"""Confirmamos nuestra hipotesis"""

def op_oculta(num):
    return num*9

for n in range (3,10):
    print(f'{n} = {op_oculta(n)}')
