# Problem 017 - Number Letter Counts
## Enunciado
Si los números del 1 al 5 se escriben en palabras (uno, dos, tres, cuatro, cinco), entonces hay un total de 3 + 3 + 5 + 4 + 4 = 19 letras usadas en total (sin contar espacios ni guiones).

¿Cuántas letras se usarían si todos los números del 1 al 1000 (inclusive) se escribieran en palabras en inglés?

👉 [Enlace al problema original](https://projecteuler.net/problem=17)

## Enfoque
La solución consiste en construir un mapeo entre números y sus representaciones en palabras en inglés (por ejemplo, `1: "one"`, `40: "forty"`, etc.). Luego, para cada número del 1 al 1000:

1. Se convierte a su forma en palabras.
2. Se eliminan espacios y se cuentan solo las letras.
3. Se acumulan los conteos individuales.

La función principal sigue una estructura condicional para manejar los diferentes rangos:

* Números del 1 al 20 y múltiplos de 10 hasta 90 se obtienen directamente del diccionario.
* Números menores a 100 se dividen en decenas y unidades.
* Números menores a 1000 se dividen en centenas y resto, añadiendo la conjunción **"and"** si corresponde (según las reglas del inglés británico).
* El número 1000 se maneja como un caso especial (`"one thousand"`).

## Resultado esperado
La suma total de letras utilizadas para escribir todos los números del 1 al 1000 en palabras es: **21124**

## Conceptos aplicados
* Diccionarios (`dict`) para mapeo palabra-número
* División entera (`//`) y módulo (`%`) para descomponer números
* Recursividad controlada para reutilizar lógica
* Cadenas (`str`) y métodos como `.replace()` para limpiar espacios
* Validación de entrada con condicionales (`if`)
* Pensamiento algorítmico sobre reglas gramaticales del idioma
