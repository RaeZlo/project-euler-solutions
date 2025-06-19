# Problem 022 - Names Scores
## Enunciado
Usando **names.txt**, un archivo de texto que contiene más de cinco mil nombres, empieza por ordenarlos alfabéticamente. Luego, calcula el valor alfabético de cada nombre y multiplícalo por su posición en la lista (empezando en 1).

Por ejemplo, si la lista ordenada es:
`["COLIN", ...]`,
COLIN es la posición 938 en la lista.
Su valor alfabético es: `3 + 15 + 12 + 9 + 14 = 53`
→ Puntuación del nombre = `938 × 53 = 49714`

¿Cuál es la suma total de todas las puntuaciones de los nombres en el archivo?

👉 [Enlace al problema original](https://projecteuler.net/problem=22)

## Enfoque
La estrategia para resolver este problema se dividió en tres pasos principales:

1. **Leer y limpiar el archivo**:

   * Se usa `open()` para leer el contenido del archivo `names.txt`.
   * Se eliminan las comillas dobles de los nombres y se dividen por comas.
   * Se filtran nombres vacíos para evitar errores al calcular puntuaciones.

2. **Ordenar alfabéticamente**:

   * Se ordena la lista de nombres con `sorted()` para asignar correctamente las posiciones.

3. **Calcular el valor de cada nombre**:

   * Se utiliza `ord(char)` para obtener el valor ASCII de cada letra y se ajusta para que `A=1`, `B=2`, ..., `Z=26`.
   * Se multiplica el valor de cada nombre por su posición en la lista.
   * Se acumula la suma total.

Este ejercicio me ayudó a **comprender mejor el trabajo con ficheros en Python** y a **entender cómo funciona la función `ord()`**, que convierte caracteres en sus códigos ASCII, lo cual fue clave para calcular el valor alfabético de cada nombre.

## Resultado esperado
La suma total de todas las puntuaciones de los nombres en el archivo es: 871198282

## Conceptos aplicados
* Lectura de archivos con `open()` y uso de context managers.
* Limpieza de strings (eliminación de comillas y espacios).
* Ordenamiento de listas alfabéticamente.
* Uso de `ord()` para convertir letras en valores numéricos.
* Comprensiones de listas y generadores.
* Enumeración con índice usando `enumerate(start=1)`.
* Acumulación eficiente con `sum()`.
* Tipado estático (`list[str]`) y funciones bien organizadas.
