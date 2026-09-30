# ProyectoPythonIA

Lo que hemos hecho ha sido buscar los datos que esten repetido y los valores vacios para trabajar con ellos, en cada caso hemos hecho lo necesario con ellos:

Eliminación de duplicados (df.drop_duplicates()): Hemos localizado y eliminado más de 100 filas que estaban repetidas de manera idéntica, evitando que ciertos pasajeros contasen doble en los promedios.

Diagnóstico de valores ausentes (df.isna().sum()): Hemos escaneado las 891 filas para cuantificar con exactitud cuántos valores nulos (NaN) tenía cada columna.
.Isna y :Sum son los encargados de saber cuantas columnas hay libres, ya que :Isna devuelve true o false depende de si la celda esta llena o vacia, eso tiene un valor(True=1, false=0) que .sum se encargad de sumar para saber cuantas casillas están vacias.

Eliminación de la columna deck: Hemos detectado que a la variable de cubierta le faltaba más del 70% de la información, así que la he eliminado por completo con .drop() porque inventarse tantos datos falsearía el estudio.
Cada deck es una columna, por eso hemos eliminado todas las columnas, asi eliminamos esta columna.

Imputación de la edad (age): He rellenado los huecos vacíos de edad con la mediana mediante .fillna(). He elegido la mediana frente a la media para evitar distorsiones por edades extremas sin perder pasajeros por el camino.
Hacemos esto porque la media iba a ser una edad no realista, por eso usamos la mediana para que la "Edad" no se deje llevar por los extremos. Esta no la eliminamos porque se pide tener esta columna.

Imputación de puertos (embarked / embark_town): Al faltar solo 2 registros en variables de texto, los he rellenado con la moda (el puerto más repetido, Southampton).

Control de calidad (df.isna().sum() y df.duplicated().sum()): He ejecutado una comprobación final demostrando que el dataset ha quedado con cero nulos y totalmente listo para que el siguiente grupo pueda continuar con el análisis.
