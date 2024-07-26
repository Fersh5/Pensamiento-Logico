# 11. **Reduce el numero a 1**
'''
En este desafío vas a recibir un número que tendrás que reducir a uno en la menor cantidad de pasos posibles aplicando las siguientes opreraciones:

* Si es número par puedes divdir por 2
* Si es número impar puedes sumar 1 o restar 1. (n+1) o (n-1).
'''
# Desarrollo
'''
El ejercicio esta hecho para ser probado para recibir un 15 y llegar a uno en el menor numero de operaciones.

# > Me parecia mas interesante hacer el ejercicio general y que independientemente del numero que se le de 
# y con las reglas establecidas siempre encuentre el menor numero de operaciones para llegar a 1.

* Dicho lo anterior a continuacion mi propuesta de solucion:
'''
def reducir(num):
    if num == 1:
        return 0
    if num < 1:
        return f'Proporciona un numero mayor que 0'
    cont=0
    while num >= 2:
        if num % 2 == 1:
            ns = num + 1
            nr = num - 1
            npar_s = [n for n in range(0,int(ns+1)) if n%2 == 0]
            npar_r = [n for n in range(0,int(nr+1)) if n%2 == 0]
            comp_s=npar_s[-1] / 2
            comp_r=npar_r[-1] / 2
            if comp_s == 1 or comp_r == 1:
                cont +=2
                return cont
            if comp_s % 2 == 0 and comp_r % 2 == 0:
                if comp_s > comp_r:
                    num+=1
                    cont+=1
                else:
                    num-=1
                    cont+=1                 
            elif comp_s % 2 ==0:
                num+=1
                cont+=1
            else:
                num-=1
                cont+=1
        else:
            num/=2
            cont+=1
        if num == 1:
            return cont
     
print (reducir(15))
print (reducir(2))
print (reducir(12))
print (reducir(41))
print (reducir(249))