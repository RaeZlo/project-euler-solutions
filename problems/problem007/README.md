## Problem 007 - 10001st Prime

### Enunciado
Al listar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, vemos que el sexto primo es 13.
El objetivo es encontrar cuál es el **primo número 10001**.

👉 [Enlace al problema original](https://projecteuler.net/problem=7)

### Enfoque
La estrategia consiste en recorrer los números naturales y verificar, uno por uno, si son primos.
A medida que se encuentran números primos, se lleva un conteo hasta alcanzar el índice deseado (10001 en este caso).

Para verificar si un número es primo se utiliza un método eficiente:

* Se descartan números menores a 2 y pares mayores a 2.
* Se prueba la divisibilidad solo hasta la raíz cuadrada del número (`√n`), y únicamente con números impares.

Este enfoque es efectivo porque:

* Evita cálculos innecesarios (no evalúa pares ni múltiplos evidentes).
* No se guarda una lista de primos, por lo tanto es **espacialmente eficiente**.
* Escala bien hasta valores moderadamente altos (como el 10001° primo).

### Resultado esperado

El primo número 10001 es: **104743**

### Conceptos aplicados
* Funciones y separación de lógica (primalidad vs. conteo)
* Bucle `while` para iterar hasta encontrar el valor objetivo
* Verificación de primalidad con optimización por raíz cuadrada
* Eficiencia en control de flujo y condiciones
* Buenas prácticas: nombres descriptivos, código limpio y modular

