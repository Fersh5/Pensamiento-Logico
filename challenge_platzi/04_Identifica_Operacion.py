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

## Bonus
'''
Vamos a tomar como base los números del 3 al 8 para multiplciarlos por un mismo factor desconocido (x) que nos da ciertos resultados.

Entonces, dada una función que recibe un array númerico con los resultados debes encontrar el factor multiplicador (x) para obtener ese resultado multiplicando por los números del 3 al 8.

* Si si un solo factor multiplicador difiere del resto se regresa false.

* En el siguiente ejemplo la función regresaria false porque hay una resultado que tiene como factor multiplicador el 6 en lugar del 9 como el resto.

* 3 * x =  27
* 4 * x =  36
* 5 * x =  45
* 6 * x =  54
* 7 * 6 =  42 <- 👈
* 8 * x =  72

Input:
```
solution([27, 36, 45, 54, 63, 72])
solution([27, 36, 45, 54, 42, 72])
```
Output:
```
9
false
```
'''
lista1 = [27,36,45,54,63,72]
lista2 = [27,36,45,54,42,72]
def solution(lista):
    fact_v = list(range(3,9))
    result = [lista[i]/fact_v[i] for i in range(0,len(lista))]
    if len(set(result)) == 1:
        return set(result).pop()
    return False

print(solution(lista1))
print(solution(lista2))