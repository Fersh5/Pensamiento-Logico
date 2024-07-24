# 08. **Identifica la Operación**
'''
Encuentra la lógica en las siguientes operaciones y números:

3 + 2 = 33
4 + 8 = 288
5 + 3 = 3,140
6 + 3 = 46,674
'''
## Desarrollo
'''
> He de confesar que me hicieron sacar lapiz y papel... ya me estaba decepcionando.

1. Primero al igual que en los anteriores busque alguna secuencia de elemento por elemento y la forma en que crecen.
2. Lo primero, podemos ver que el primer elemento va de uno en uno del 3 al 6 y a la derecha del '=' crece de forma muy acelerada.
3. Al principio me deje llevar por la inercia de los ejercicios anteriores es decir, concatenando operaciones.
4. El truco estaba en el primer elemento que iba de uno a uno y el rapido crecimiento del otro lado de la igualdad.
5. Si se eleva el primer elemento a si mismo tenemos ya una gran aproximacion.

* 3^3 = 27
* 4^4 = 256
* 5^5 = 3,125
* 6^6 = 46,656

6. Ahora hacemos la diferencia que hay entre cada operacion esperando encontrar un pantron.
33 - 27 = 6
288 - 256 = 32
3,140 - 3,125 = 15
46,674 - 46,656 = 18

7. Ahí esta, ese resultado coincide con la multiplicacion del primer elemento con el segundo.

'''
## Solucion
'''
* La espreción resultante seria la siguiente:

___n1 + n2 = (n1^n1) + n1*n2___
'''

def ope(n1,n2):
    return n1**n1 + n1*n2
element1 = list(range(3,7))
element2 = [2,8,3,3]
for i in range(len(element1)):
    print(f'{element1[i]} + {element2[i]} = {ope(element1[i],element2[i])}')