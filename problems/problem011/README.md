## Problem 011 - Largest Product in a Grid
### Enunciado
En una cuadrícula de 20×20 como la siguiente, ¿cuál es el mayor producto de **cuatro números adyacentes** en la misma dirección (arriba, abajo, izquierda, derecha o en diagonal)?

```
08 02 22 97 38 ...
49 49 99 40 17 ...
...
01 70 54 71 83 ...
```

👉 [Enlace al problema original](https://projecteuler.net/problem=11)

### Enfoque
La estrategia consiste en convertir la cadena de texto que representa la cuadrícula en una lista de listas de enteros, y luego recorrer cada celda evaluando los productos posibles en las cuatro direcciones principales:

* **Horizontal (→)**
* **Vertical (↓)**
* **Diagonal derecha (↘)**
* **Diagonal izquierda (↙)**

Para cada celda del grid, se verifica si es posible calcular un producto de 4 elementos en esa dirección (es decir, que no se salga de los límites), y si es así, se evalúa el producto. Se mantiene el valor máximo encontrado.

La lógica se encapsula en funciones para mantener el código claro y reutilizable.

### Resultado esperado
El mayor producto de cuatro números adyacentes en la misma dirección en la cuadrícula proporcionada es: **70600674**

### Conceptos aplicados
* Conversión de string multilinea a matriz numérica (`parse_grid`)
* Recorrido sistemático con bucles anidados
* Cálculo de producto de elementos (`product`)
* Evaluación condicional para evitar desbordes de índice
* Comparación y actualización de valores máximos
* Encapsulamiento en funciones auxiliares
* Tipado con `List[int]` y documentación con docstrings
* Modularidad y legibilidad
