# 06. Operaciones Matematicas
'''
Encuentra la lógica en las siguientes operaciones y números
3 + 2 = 91
5 + 4 = 251
9 + 3 = 366
8 + 6 = 562
'''
## Desarrollo
'''
Primeramente hay que buscar una relacion que sigan todas las operaciones, que sea congruente y concuerde con cada una de ellas.
> No Existe una forma directa de llegar con la solucion, toca probar e intentar, inclusive pueda que haya mas de una respuesta. En este ejercicio explicare la forma en la que yo llegue al resultado, sin embargo pueden existir metodos mas sencillos o faciles de entender.

* Como comentaba tiene algun sentido ***'3 + 2 = 91'*** debe existir alguna forma haciendo operaciones de llegar a esa conclusion.
1. Primero, al ver que de vista es muy ambiguo, intente ver algun patron entre los demas elementos primero los primeros sumandos es decir [3,5,9,8] 
2. Al no encontrar aparente sucesion segui con los segundos sumandos [2,4,3,6]
3. Por ultimo de igual forma con los resultados [91,251,366,562]
4. Realmente si fuese un ejercicio sencillo al analizar estas partes ya deberiamos haber encontrado algun patron o directamente la solucion.
5. Al no encontrar algo significativo, lo que hice fue analizar el todo pero por parejas es decir, que tienen en comun ***'3 + 2 = 91'*** y ***'5 + 4 = 251'***
6. Lo primero que identifique es que si al primer elemento le restamos el segundo obtenemos el digito de mas a la derecha, esto al realizarlo con todas la operaciones vemos que se cumple.
     3 - 2 = 1
     5 - 4 = 1
     9 - 3 = 6
     8 - 6 = 2
7. Nos queda descubrir los digitos de la izquierda. Lo primero que pense es que el primer elemento estaba elevado al cuadrado, al hacerlo en todas las operaciones, esto solo se cumple para la primera y segunda.
8. Luego me di cuenta que si multiplicamos al primer elemento por el segundo mas 1 ya coincidian.
    3 * (2+1) = 9
    5 * (4+1) = 25
    9 * (3+1) = 36
    8 * (6+1) = 56
9. Ahora solo quedaba concatenar ambos resultados en el orden correcto y listo.
'''
## Solucion
# Confirmamos nuestra hipotesis

# Objetivo
'''
3 + 2 = 91
5 + 4 = 251
9 + 3 = 366
8 + 6 = 562
'''
def operacion(num1, num2):
    return f'{num1 * (num2 + 1)}{num1 - num2}'
'''
Cabe destacar que en el ejercicio todas las operaciones el primer elemento es mayor que el segundo, y ya que se modelo solo usando esos datos. 
Si ponemos el segundo elemento mayor que el primero, la resta dará negativo y al tener el signo '-' en el medio del resultado 
al intentar hacer la conversion a tipo int dará error
'''

print(f'3 + 2 = {int(operacion(3,2))}')
print(f'5 + 4 = {int(operacion(5,4))}')
print(f'9 + 3 = {int(operacion(9,3))}')
print(f'8 + 6 = {int(operacion(8,6))}')
