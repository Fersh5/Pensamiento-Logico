# 03. **Carrera de Automóviles**
* Tenemos información de que el conductor José ha llegado justo detrás de Pedro, además de que Miguel  llegó en medio de Francisco y José.
* ¿Cuál es el orden de llegada de los conductores?

## Desarrollo

📝Tenemos los siguientes conductores: Jose, Pedro, Miguel y Francisco

💡Son 4 posiciones posibles
**Tenemos las siguientes verdades**
```
1. Jose llegó justo detras de Pedro 
2. Miguel llegó en medio de Francisco y Jose
```
Si posicionamos los conductores en una hipotetica recta, donde mas a la derecha es el 1er lugar y mas a la izquierda es el ultimo lugar

1. Jose, Pedro
2. Jose, Miguel, Francisco ❌ **Esta forma contradice la primer verdad ya que Jose va justo detras de Pedro**
2. Francisco, Miguel, Jose ✅ **Esta forma puede convivir con la primer verdad**

## Solucion

1. Jose, Pedro
2. Francisco, Miguel, Jose

***Resultado:***
1. ***Pedro***
2. ***Jose*** 
3. ***Miguel*** 
4. ***Francisco***