# 12. **Imprime los Numeros Primos**
'''
En este desafío te damos como entrada un número positivo mayor a cero y debes regresar un arreglo 
con todos los números primos menores o iguales a ese número de entrada ordenados de menor a mayor.
'''
## Desarrollo
'''
* Recuerda que un número es primo si es solo divisible por 1 y por si mismo.
'''
## Solucion propuesta

def num_primo(num):
    primos=[]
    for num in range(2, num+1):
        primo=[]
        base=num
        for num in range(1, num+1):
            if base % num == 0:
                primo.append(base)
        if len(primo) == 2:
            primos.append(primo.pop())
    return primos
        
num_primo(50)
