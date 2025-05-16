# Problem 008 - Greatest Product in a Series
## Enunciado
El enunciado plantea encontrar el mayor producto de una cantidad determinada de dígitos consecutivos dentro de una larga cadena de números.

Por ejemplo, en una serie como `123456789`, el producto de 5 dígitos consecutivos más grande sería `5×6×7×8×9 = 15120`.

El objetivo es aplicar esta lógica sobre una secuencia mucho mayor (de 1000 dígitos), y determinar cuál es el mayor producto posible para 13 dígitos consecutivos.

👉 [Enlace al problema original](https://projecteuler.net/problem=8)

## Enfoque
La estrategia consiste en recorrer la serie con una ventana deslizante (sliding window) de tamaño `length` (13 por defecto), evaluando el producto de los dígitos dentro de esa ventana.

Se ignoran aquellas ventanas que contengan el dígito `0`, ya que su producto será automáticamente cero, lo cual ayuda a optimizar ligeramente el proceso.

### Este enfoque es eficiente porque:
- No almacena todos los productos posibles, solo mantiene el máximo actual.
- Utiliza una simple comparación en cada paso para actualizar el valor máximo.
- Aprovecha la propiedad de que cualquier número multiplicado por 0 da 0, para saltar subsecuencias innecesarias.

## Resultado esperado
Para la serie original de 1000 dígitos y una longitud de 13 dígitos consecutivos, el producto mayor es: **23514624000**

## Conceptos aplicados
- Bucles `for`
- Substrings
- Condicionales (`if`)
- Conversión de caracteres a enteros
- Producto acumulativo
- Optimización con early `continue`
- Pensamiento algorítmico (ventana deslizante)
