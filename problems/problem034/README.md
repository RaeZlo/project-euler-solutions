# Problem 034 - Digit Factorials
## Enunciado
Encuentra la suma de todos los números que son iguales a la suma del factorial de sus dígitos.
Por ejemplo, 145 es un número curioso ya que:

1! + 4! + 5! = 1 + 24 + 120 = 145

Nota: 1! y 2! no deben ser considerados como sumas.

👉 [Enlace al problema original](https://projecteuler.net/problem=34)

## Enfoque
El problema se puede abordar iterando sobre todos los números desde 10 hasta un cierto **límite superior** y verificando si el número es igual a la suma del factorial de sus dígitos.

Se realiza un **precálculo** de los factoriales de los dígitos del 0 al 9 para evitar recomputarlos en cada iteración, lo que mejora la eficiencia del algoritmo.

El rango superior elegido (por defecto `1_000_000`) es suficiente para encontrar todos los números que cumplen esta condición. De hecho, se sabe que el máximo teórico está por debajo de `7 × 9! = 2_540_160`, ya que un número de n cifras no puede exceder la suma de n veces 9!.

### Pasos del enfoque:
1. Precalcular los factoriales de los dígitos del 0 al 9.
2. Iterar desde 10 hasta un límite superior.
3. Para cada número, sumar los factoriales de sus dígitos.
4. Si el resultado es igual al número original, acumularlo en el total.
5. Devolver la suma total.

## Resultado esperado
La suma de todos los números que cumplen con esta condición es: **40730**

## Conceptos aplicados
* Precalculación de resultados para evitar operaciones repetidas.
* Transformación de números en cadenas para iterar sobre sus dígitos.
* Uso de comprensión de listas y generadores.
* Comparación entre un número y su descomposición matemática.
* Tipado estático (type hints) y buenas prácticas de codificación.
