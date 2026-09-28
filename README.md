# ProyectoPythonIA

Nuestro labor ha consistido en sanear los datos para que las conclusiones posteriores no estén falseadas por registros repetidos o valores vacíos:

Eliminación de duplicados (df.drop_duplicates()): He localizado y eliminado más de 100 filas que estaban repetidas de manera idéntica, evitando que ciertos pasajeros contasen doble en los promedios.

Diagnóstico de valores ausentes (df.isna().sum()): He escaneado las 891 filas para cuantificar con exactitud cuántos valores nulos (NaN) tenía cada columna.

Eliminación de la columna deck: He detectado que a la variable de cubierta le faltaba más del 70% de la información, así que la he eliminado por completo con .drop() porque inventarse tantos datos sesgaría el estudio.

Imputación de la edad (age): He rellenado los huecos vacíos de edad con la mediana mediante .fillna(). He elegido la mediana frente a la media para evitar distorsiones por edades extremas sin perder pasajeros por el camino.

Imputación de puertos (embarked / embark_town): Al faltar solo 2 registros en variables de texto, los he rellenado con la moda (el puerto más repetido, Southampton).

Control de calidad (df.isna().sum() y df.duplicated().sum()): He ejecutado una comprobación final demostrando que el dataset ha quedado con cero nulos y totalmente listo para que el siguiente grupo pueda continuar con el análisis.
