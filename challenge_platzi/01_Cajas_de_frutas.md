# Problema: **Cajas de Futas**
Tengo 3 cajas, cada una contiene un tipo de fruta diferente (peras, manzanas y naranjas). El problema es que **todas las cajas tienen las etiquetas de las frutas incorrectas.** ¿Cuántas cajas necesito abrir para saber colocar todas las etiquetas correctamente?

## Desarrollo

📝 ***El ejercicio nos da la clave al indicar que todas las cajas tienen una etiqueta erronea.***


> "🍐🍎🍊" --> Representa contenido

> "Texto"  -->  Representa etiqueta

```
🍐 --> Peras
🍎 --> Manzanas
🍊 --> Naranjas
```

💡 ***Solo sabemos que ninguna etiqueta corresponde al contenido de las cajas***

```
○ --> Peras
○ --> Manzanas
○ --> Naranjas
```

Pensemos que abrimos la caja con la etiqueta "Peras" y esta contiene "🍎".

```
🍎--> Peras
○ -->  Manzanas
○ -->  Naranjas
```

* Ya sabiamos que la etiqueta "Naranjas" no contiene "🍊".
* Ahora sabemos que la etiqueta "Peras" tampoco contiene naranjas.
* Conclusion las "🍊" estan en la etiqueta "Manzanas"

Con lo que de momento las cosas van asi:

```
🍎--> Peras
🍊--> Manzanas
○ -->  Naranjas
```

* Solo queda descubrir la fruta que nos falta, es decir "🍐"

```
🍎 --> Peras
🍊 -->  Manzanas
🍐 -->  Naranjas
```

## Solucion

***Respuesta: solo requerimos abrir una caja para colocar las etiquetas correctamente***

```
🍎 --> Manzanas
🍊 --> Naranjas
🍐 --> Peras
```