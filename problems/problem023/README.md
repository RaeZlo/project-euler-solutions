# Problem 023 - Non-abundant sums
## Enunciado
Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el mismo número) es igual al número.  
Un número deficiente tiene una suma menor, y uno abundante, una suma mayor.

Se puede demostrar que **todos los enteros mayores a 28123 pueden escribirse como la suma de dos números abundantes**.

**¿Cuál es la suma de todos los enteros positivos que no pueden escribirse como la suma de dos números abundantes?**

👉 [Enlace al problema original](https://projecteuler.net/problem=23)

## Enfoque
La estrategia se divide en tres pasos:

1. **Detectar los números abundantes** hasta el límite (28123), es decir, aquellos cuya suma de divisores propios es mayor que el número.

2. **Marcar todas las sumas posibles** entre pares de números abundantes. Para esto, se usa una lista booleana de tamaño 28123+1, donde cada índice representa si ese número puede ser generado como suma de dos abundantes.

3. **Sumar todos los números** que no han sido marcados como suma de dos abundantes. Estos son los que buscamos.

Este enfoque es eficiente porque:

- Se precomputan los divisores usando optimización hasta la raíz cuadrada.
- Se evita recomputar sumas imposibles con un corte temprano (`break`) si la suma excede el límite.
- El uso de una lista booleana permite marcar eficientemente las combinaciones válidas.

## Resultado esperado
La suma de todos los enteros positivos que **no pueden** escribirse como la suma de dos números abundantes es: **4179871**

## Conceptos aplicados
- Iteración con comprensión de listas
- Optimización en el cálculo de divisores
- Uso de `range` con control de límites
- Estructuras booleanas para marcado eficiente
- Bucles anidados con control de corte (`break`)
- Pensamiento matemático (números abundantes, divisores propios, propiedades numéricas)
