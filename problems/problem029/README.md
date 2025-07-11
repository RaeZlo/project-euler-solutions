# Problem 029 - Distinct Powers
## Enunciado
Considerando todos los números generados por la expresión \( a^b \), donde:

- \( 2 \leq a \leq 100 \)
- \( 2 \leq b \leq 100 \)

¿Cuántos resultados distintos se pueden obtener?

Por ejemplo, si \( a \) y \( b \) están entre 2 y 5:

- Los términos generados incluyen: 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 125, 216, 256, 625.
- Algunos valores se repiten, como \( 2^4 = 4^2 = 16 \).

Por lo tanto, se busca contar cuántos valores únicos se generan en total para todos los \( a^b \) posibles en ese rango.

👉 [Enlace al problema original](https://projecteuler.net/problem=29)

## Enfoque
La idea es generar todos los posibles valores de la forma \( a^b \) en los rangos dados y utilizar un conjunto (`set`) para eliminar duplicados.

Los pasos son:

1. Iterar sobre todos los valores de `a` en el rango [2, a_max].
2. Iterar sobre todos los valores de `b` en el rango [2, b_max].
3. Calcular \( a^b \) y agregarlo a un conjunto.
4. Al final, contar cuántos elementos únicos hay en ese conjunto.

Este enfoque es directo y funciona muy bien para rangos hasta 100 porque:

- Utiliza **set comprehension**, que es eficiente y conciso.
- No necesita ordenamiento ni estructuras complejas.
- La eliminación automática de duplicados está garantizada por el conjunto.

## Resultado esperado
El resultado correcto para `a_max = 100` y `b_max = 100` es: **9183**

## Conceptos aplicados
- **Set comprehension**
- **Operaciones aritméticas (potencias)**
- **Estructuras de datos eficientes (`set`)**
- **Eliminación de duplicados**
- **Pensamiento algorítmico y matemático**
