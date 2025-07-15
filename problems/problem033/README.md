# Problem 033 - Digit Cancelling Fractions
## Enunciado
La fracción 49/98 es un ejemplo interesante: al cancelar el 9 de forma incorrecta en el numerador y el denominador se obtiene 4/8, que es equivalente a la fracción original.

Se busca encontrar **todas las fracciones de dos cifras no triviales** (es decir, que no terminan en 0) para las cuales esta forma incorrecta de cancelación produce una fracción equivalente a la original.

Una vez encontradas, se deben multiplicar entre sí y simplificar el resultado a su forma más simple.
👉 [Enlace al problema original](https://projecteuler.net/problem=33)

## Enfoque
El problema se resuelve buscando todas las fracciones `a/b` donde:

* `10 ≤ a < b < 100` (fracciones propias de dos cifras)
* El numerador y denominador comparten al menos un dígito **no trivial** (que no sea '0').
* Al eliminar ese dígito común de ambos, el resultado debe ser **una fracción válida y equivalente**.

El algoritmo consiste en:

1. **Iterar** por todos los posibles numeradores y denominadores de dos cifras.
2. **Descartar** casos triviales (como 30/50).
3. **Verificar** si la cancelación de un dígito compartido da como resultado una fracción equivalente.
4. **Multiplicar** todas las fracciones válidas encontradas.
5. **Simplificar** la fracción resultante utilizando el máximo común divisor (`gcd`).
6. **Devolver el denominador** de la fracción en su forma reducida.

## Resultado esperado
El denominador de la fracción resultante en su forma más simple es: **100**

## Conceptos aplicados
* Conversión entre tipos (`int`, `str`) para manipular y comparar dígitos.
* Verificación de igualdad entre fracciones con `float` y tolerancia de error.
* Uso de `math.gcd()` para simplificar fracciones.
* Comparación precisa con `abs(a - b) < 1e-9` para evitar errores por coma flotante.
* Buenas prácticas de programación:
  * Tipado estático (`int`) y funciones pequeñas con responsabilidades claras.
  * Nombres descriptivos para mejorar la legibilidad.
  * Separación de lógica (`is_digit_cancelling`) y ejecución principal (`solve`).

## Aprendizaje personal
Este problema me ayudó a entender cómo detectar patrones matemáticos poco comunes (cancelación de dígitos incorrecta pero válida), y cómo aplicar aritmética con validaciones precisas. También reforcé la importancia de evitar comparaciones exactas con `float` y de utilizar el `gcd` para reducir fracciones. Además, implementé una solución clara y modular, siguiendo buenas prácticas y dejando espacio para testeo automatizado y futura extensión del código.