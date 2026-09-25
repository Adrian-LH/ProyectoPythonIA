# ProyectoPythonIA
## T1 - Carga e inspección inicial

### Qué es esta parte y para qué sirve
Antes de poder limpiar datos, crear columnas o sacar conclusiones, hay que
cargar el dataset y echarle un primer vistazo: cuántas filas tiene, qué
columnas hay, de qué tipo son y si les falta algún dato. Esta parte es la
base de todo lo que viene después, así que si vas a trabajar en las
siguientes tareas, empieza por entender lo que se explica aquí.

### Cómo se cargó el dataset
Se usó la librería **seaborn**, que trae varios datasets de ejemplo ya
preparados. Con esta línea se descarga y se guarda en una variable llamada
`df` (abreviatura de "DataFrame", que es como pandas llama a sus tablas):

```python
df = sns.load_dataset("titanic")
```

A partir de aquí, `df` es la tabla completa con la que se trabaja en todo
el notebook. Cada fila es un pasajero del Titanic, y cada columna es un
dato suyo (edad, sexo, clase del billete, si sobrevivió...).

### Qué se hizo para inspeccionarlo
No hace falta imprimir todo el dataset para hacerse una idea de él; para
eso están estos cuatro comandos:

- **`df.head()`**: muestra las 5 primeras filas, a modo de muestra rápida
  de cómo son los datos y qué aspecto tiene cada columna.
- **`df.info()`**: da un resumen de la tabla entera, columna por columna:
  cuántos valores tiene cada una que **no** son nulos, y de qué tipo son
  (número entero, decimal, texto...). Es el comando más importante de
  esta parte, porque aquí es donde se detecta qué columnas tienen huecos.
- **`df.describe()`**: calcula estadísticas básicas (media, mínimo,
  máximo, cuartiles...) mas solo de las columnas numéricas. Sirve para
  hacerse una idea de los rangos de valores, por ejemplo que la edad va
  de bebés hasta 80 años.
- **`df.shape`**: da directamente el número de filas y columnas, sin
  tener que contarlas a mano.

### Resultado de la inspección
El dataset tiene **891 filas y 15 columnas**. Cada fila es un pasajero.

- **Columnas numéricas:** `survived` (0 = no sobrevivió, 1 = sobrevivió),
  `pclass` (clase del billete), `age`, `sibsp` (hermanos/cónyuges a
  bordo), `parch` (padres/hijos a bordo), `fare` (precio del billete).
- **Columnas categóricas o de texto:** `sex`, `embarked`, `class`, `who`,
  `deck`, `embark_town`, `alive`, y un par de columnas de verdadero/falso
  como `adult_male` y `alone`.

### Lo importante para quien siga con la siguiente parte
Al ejecutar `df.info()` se ve que hay columnas con valores nulos (huecos
sin dato):

- **`age`**: le faltan bastantes valores (unos 177 de 891).
- **`deck`**: es la que más huecos tiene, con diferencia (faltan más de
  dos tercios de los datos).
- **`embarked`** y **`embark_town`**: solo les faltan un par de valores.

Esto es justo lo que hay que tratar en la siguiente tarea (detectar y
tratar nulos y duplicados): decidir si esos huecos se rellenan, se
eliminan, o si directamente conviene descartar la columna (como pasa con
`deck`, que tiene tan pocos datos que rellenarla no aportaría mucho).