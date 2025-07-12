# Problem 030 - Digit Fifth Powers
## Enunciado
El problema plantea encontrar todos los números que pueden ser escritos como la **suma de las potencias de sus dígitos**.

Por ejemplo:
`4150 = 4⁵ + 1⁵ + 5⁵ + 0⁵`
`4151 = 4⁵ + 1⁵ + 5⁵ + 1⁵`

El objetivo es identificar todos los números que cumplan esta condición para una potencia determinada (por defecto, 5) y calcular la suma total de dichos números.

👉 [Enlace al problema original](https://projecteuler.net/problem=30)

## Enfoque
La estrategia se basa en:

1. **Elevar cada dígito de un número a una potencia dada (`power`)**.
2. Sumar esas potencias.
3. Verificar si esa suma es igual al número original.

Si se cumple esta igualdad, el número es válido y se guarda.

### Cálculo del límite de búsqueda
Para optimizar el rango de búsqueda y evitar iterar infinitamente, se define un **límite superior lógico**:

```
search_limit = (9 ** power) * power
```

Esto se basa en que:

* El dígito más alto es 9.
* Si tomamos `n` dígitos, el máximo valor que la suma de sus potencias puede alcanzar es `n * 9^power`.
* Si ese valor deja de tener la misma cantidad de dígitos que `n`, ya no puede ser igual al número original, y se corta la búsqueda.

Este enfoque acota eficientemente el espacio de búsqueda sin necesidad de recorrer todos los números posibles.

## Resultado esperado
Para `power = 5`, los únicos números que cumplen la condición son:
`4150`, `4151`, `54748`, `92727`, `93084`

La suma total de estos números es: **443839**

## Conceptos aplicados
* Diccionarios para evitar cálculos repetidos (`{d: d**power}`)
* Compresión de listas
* Comparación numérica
* Conversión de enteros a strings para iterar sobre dígitos
* Pensamiento algorítmico
* Optimización del espacio de búsqueda
* Validación de entrada para casos límite (potencias menores a 1)