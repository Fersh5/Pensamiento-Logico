# 13. **Logica del mandato**
'''
Descripción del reto

* ¿Cuántas veces puede restarse el número 3 del número 3,333?
'''
## Desarrollo
'''
* Cuando hablamos de cuantasveces puede restarse el numero 3 en 3,333 es lo mismo que decir cuantas veces cabe el 3 en 3,3333.
* Suena mas familiar y exactamente es una simple division.
* Y si queda duda lo podemos comprobar.
'''
## Solucion
def cuenta_resta(n_menor,base):
    cont_resta=0
    base_1=base
    while(base>=n_menor):
        base-=n_menor
        cont_resta+=1
    # Forma de division
    cont_div = base_1 // n_menor
    return print(f'Si restamos el {n_menor} en {base_1} cabe {cont_resta} \nSi lo hacemos dividiendo da {cont_div}\n')

cuenta_resta(3,3333)
cuenta_resta(5,52)

## Correccion
'''
> Parece que de nuevo me equivoque... jaja

* La resouesta correcta es 1 !!

¿ Como llegamos a esta conclusion ? Leamos de nuevo la oracion:

* ¿Cuántas veces puede restarse el número 3 del número 3,333?

* Pues al restarse 3 a 3,333 da 3,330 por lo que al ser un numero distinto no puede restarsele de nuevo.

🙃🙃🙃🤡🤡🤡🙃🙃🙃
'''