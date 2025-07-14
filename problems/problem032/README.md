# Problem 032 - Pandigital Products
## Enunciado
Podemos decir que una identidad como 39 × 186 = 7254 es **pandigital** porque usa exactamente todos los dígitos del 1 al 9 una sola vez.

Encuentra la suma de todos los productos cuyos factores multiplicados pueden escribirse como una identidad pandigital de 1 a 9.

**Nota**: Algunos productos pueden obtenerse de más de una forma, pero solo deben contarse una vez.

👉 [Enlace al problema original](https://projecteuler.net/problem=32)

## Enfoque
La estrategia consiste en probar todas las combinaciones de multiplicando, multiplicador y producto que juntos formen una cadena con **9 dígitos pandigitales** (usando cada dígito del 1 al 9 una sola vez, sin ceros ni repeticiones).

Para abordar esto de forma eficiente:

* Se evalúan dos **casos posibles** según la longitud de los factores y el producto:

  * Caso 1: 1 dígito × 4 dígitos = 4 dígitos → ej: 2 × 3457 = 6914
  * Caso 2: 2 dígitos × 3 dígitos = 4 dígitos → ej: 39 × 186 = 7254
* Para cada combinación, se concatenan los factores y el producto, y se verifica si forman un número pandigital.
* Se utiliza un `set` para **evitar contar productos repetidos**.
* La verificación de pandigitalidad se encapsula en una función auxiliar.
* El código está organizado en funciones pequeñas y testeadas con `unittest`.

## Resultado esperado
La suma de todos los productos pandigitales únicos es: **45228**

## Conceptos aplicados
* Generación y verificación de combinaciones numéricas.
* Uso de `set` para eliminar duplicados.
* Manipulación de strings y verificación pandigital.
* Funciones auxiliares reutilizables para claridad y mantenimiento.
* Separación de lógica en funciones testeables.
