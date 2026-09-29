# P1 — Análisis exploratorio del dataset Titanic

Actividad P1 de la optativa **Python para IA** (2º DAM). Análisis exploratorio con `numpy` y `pandas`.

## Dataset

Se usa el dataset recomendado por la actividad: los **pasajeros del Titanic**, cargado directamente desde `seaborn`:

```python
import seaborn as sns
df = sns.load_dataset("titanic")
```

Tiene 891 filas y 15 columnas (edad, sexo, clase del billete, tarifa, puerto de embarque, si sobrevivió, etc.).

## Contenido

- `titanic_analisis.ipynb`: notebook con el código comentado y organizado por tareas:
  - **T1** Carga e inspección (`head`, `info`, `describe`, `shape`)
  - **T2** Limpieza: duplicados y valores nulos, con su justificación
  - **T3** Transformación: columna derivada `age_group` con `np.select`
  - **T4** Análisis: filtros, `groupby` y más de 5 estadísticas
  - **T5** Conclusiones y respuestas a las preguntas guía

## Tratamiento de datos

- **Duplicados:** se eliminan 107 filas idénticas (891 → 784 pasajeros).
- **`deck`:** se elimina la columna (~74 % de nulos).
- **`age`:** 106 nulos rellenados con la mediana (28.25 años).
- **`embarked` / `embark_town`:** 2 nulos rellenados con la moda (Southampton).

## Resumen de conclusiones

1. Sobrevivió el **41.20 %** de los pasajeros: menos de la mitad.
2. El **sexo** fue el factor más determinante: **74.06 %** de las mujeres frente al **21.59 %** de los hombres.
3. La **clase** también influyó: 63.08 % en 1ª, 50.91 % en 2ª y 25.68 % en 3ª.
4. La franja de **0-12 años** tuvo la mayor supervivencia (57.35 %), pero la correlación entre edad y supervivencia es débil (-0.079).
5. Combinando **sexo y clase**, las mujeres de 1ª y 2ª superaron el 90 % de supervivencia y los hombres de 3ª solo llegaron al 15.83 %.

## Cómo ejecutarlo

```bash
pip install numpy pandas seaborn matplotlib jupyter
jupyter notebook titanic_analisis.ipynb
```





Nuestro labor ha consistido en sanear los datos para que las conclusiones posteriores no estén falseadas por registros repetidos o valores vacíos:

Eliminación de duplicados (df.drop_duplicates()): He localizado y eliminado más de 100 filas que estaban repetidas de manera idéntica, evitando que ciertos pasajeros contasen doble en los promedios.

Diagnóstico de valores ausentes (df.isna().sum()): He escaneado las 891 filas para cuantificar con exactitud cuántos valores nulos (NaN) tenía cada columna.

Eliminación de la columna deck: He detectado que a la variable de cubierta le faltaba más del 70% de la información, así que la he eliminado por completo con .drop() porque inventarse tantos datos sesgaría el estudio.

Imputación de la edad (age): He rellenado los huecos vacíos de edad con la mediana mediante .fillna(). He elegido la mediana frente a la media para evitar distorsiones por edades extremas sin perder pasajeros por el camino.

Imputación de puertos (embarked / embark_town): Al faltar solo 2 registros en variables de texto, los he rellenado con la moda (el puerto más repetido, Southampton).

Control de calidad (df.isna().sum() y df.duplicated().sum()): He ejecutado una comprobación final demostrando que el dataset ha quedado con cero nulos y totalmente listo para que el siguiente grupo pueda continuar con el análisis.
