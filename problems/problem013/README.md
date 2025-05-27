# Problem 013 - Large Sum
## Enunciado
Trabajando con números muy grandes, a veces es necesario obtener solo una parte de la suma para verificar resultados. Dado una lista de 100 números de 50 dígitos cada uno, ¿cuáles son los primeros `n` dígitos de su suma?

👉 [Enlace al problema original](https://projecteuler.net/problem=13)

## Enfoque
Se realiza una suma directa de todos los números usando la función `sum()`, ya que Python permite operar con enteros de precisión arbitraria sin pérdida de exactitud.

Una vez calculada la suma total, se convierte en cadena para extraer los primeros `n` dígitos mediante slicing.

Este enfoque es eficiente porque:

* La operación de suma en Python es precisa sin necesidad de bibliotecas externas.
* Al operar con enteros, se evita el redondeo o error asociado a los decimales.
* No se requieren estructuras adicionales ni optimización matemática específica.

## Resultado esperado
Los primeros 10 dígitos de la suma de los 100 números de 50 dígitos son: `5537376230`

## Conceptos aplicados
* Tipado estático (`list[int]`, `str`)
* Función `sum()` de Python
* Conversión entre tipos (`int` → `str`)
* Indexado y slicing de cadenas
* Precisión arbitraria de enteros en Python
* Buenas prácticas en la validación de parámetros
