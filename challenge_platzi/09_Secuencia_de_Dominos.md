# 9. **Secuencia de Dominos**
![Dominos](https://static.platzi.com/media/user_upload/Dominos-94671981-69cc-480c-902a-5d580ed984bc.jpg)

## Desarrollo

1. Solo de observar podemos decir que el numero inferior es el superior de la siguiente ficha
2. Podemos transformar los dominos a una representacion de fraccion:

* --> 4 5 0 1 3
*    ➖➖➖➖
* --> 5 0 1 3 4

3. Ahora es mas facil visualisar el patron, y ya que una ficha depende de la anterior, estos se repiten una y otra vez.

## Solucion
                   ⬇️
*  4 5 0 1 3 -->   ***4***
* ➖➖➖➖➖
*  5 0 1 3 4 -->  ***5***

## Correccion
* Aunque la respuesta anterior es consistente 
* Parece que en Platzi dan otra respuesta que tambien es congruente.
* Pensando que se suman 1 y 2 de forma intercalada tanto arriba como abajo
* Esto modifica el resultado a :
* 4
* ➖
* 6