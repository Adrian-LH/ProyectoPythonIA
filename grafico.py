import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================
# T1: CARGA E INSPECCIÓN INICIAL
# ============================================================

print("T1: CARGA E INSPECCIÓN")
print("=" * 50)

# 1. Cargar el dataset directamente
df = sns.load_dataset("titanic")

# 2. Inspección del contenido

print("\nPrimeras filas del dataset (.head()):")
print(df.head())

print("\nInformación general y tipos de datos (.info()):")
df.info()

print("\nEstadísticas descriptivas de columnas numéricas (.describe()):")
print(df.describe())

print(f"\nForma del dataset (Filas, Columnas): {df.shape}")


# ============================================================
# T2: LIMPIEZA DE DATOS
# ============================================================

print("\n" + "=" * 50)
print("T2: LIMPIEZA DE DATOS (NULOS Y DUPLICADOS)")
print("=" * 50)

# ------------------------------------------------------------
# 2.1. Detección y eliminación de duplicados
# ------------------------------------------------------------

duplicados = df.duplicated().sum()

print(f"Filas duplicadas encontradas: {duplicados}")

# Eliminamos las filas repetidas para no sesgar las estadísticas
df = df.drop_duplicates().reset_index(drop=True)

print(f"Filas tras eliminar duplicados: {df.shape[0]}")


# ------------------------------------------------------------
# 2.2. Detección de valores nulos
# ------------------------------------------------------------

print("\nValores nulos por columna antes de limpiar:")
print(df.isna().sum()[df.isna().sum() > 0])


# ------------------------------------------------------------
# 2.3. Tratamiento de valores nulos
# ------------------------------------------------------------

# Faltan más del 70% de datos; se elimina para no inventar información
if "deck" in df.columns:
    df = df.drop(columns=["deck"])
    print("\n-> Columna 'deck' eliminada por exceso de valores nulos (>70%).")


# Es una variable clave. Rellenamos huecos con la mediana
# para que los valores extremos no alteren la distribución
mediana_edad = df["age"].median()

df["age"] = df["age"].fillna(mediana_edad)

print(f"-> Nulos en 'age' rellenados con la mediana: {mediana_edad:.1f} años.")


# Faltan muy pocos valores. Se rellenan con la moda
# (el valor más común)
moda_town = df["embark_town"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(moda_town)

moda_embarked = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(moda_embarked)

print(
    f"-> Nulos en puerto de embarque rellenados con la moda: "
    f"'{moda_town}' ('{moda_embarked}')."
)


# ------------------------------------------------------------
# 2.4. Comprobación final
# ------------------------------------------------------------

print("\nComprobación de nulos tras la limpieza:")
print(df.isna().sum())

print(f"Dimensiones finales del dataset limpio: {df.shape}")


# ============================================================
# T3: TRANSFORMACIÓN DE DATOS
# ============================================================

print("\n" + "=" * 50)
print("T3: TRANSFORMACIÓN DE DATOS")
print("=" * 50)

# Crear una nueva columna agrupando a los pasajeros por edad

condiciones = [
    df["age"] <= 12,
    (df["age"] >= 13) & (df["age"] <= 17),
    (df["age"] >= 18) & (df["age"] <= 30),
    (df["age"] >= 31) & (df["age"] <= 50),
    df["age"] >= 51
]

grupos_edad = [
    "0-12",
    "13-17",
    "18-30",
    "31-50",
    "51+"
]

df["age_group"] = np.select(
    condiciones,
    grupos_edad,
    default="Sin grupo"
)

print("\nNueva columna 'age_group':")
print(df[["age", "age_group"]].head(10))

print("\nNúmero de pasajeros por grupo de edad:")
print(df["age_group"].value_counts().sort_index())


# ============================================================
# T4: ANÁLISIS DE DATOS
# ============================================================

print("\n" + "=" * 50)
print("T4: ANÁLISIS DE DATOS")
print("=" * 50)


# ------------------------------------------------------------
# 4.1. Porcentaje de supervivencia general
# ------------------------------------------------------------

supervivencia_general = df["survived"].mean() * 100

print(
    f"\n1. Porcentaje de pasajeros que sobrevivieron: "
    f"{supervivencia_general:.2f}%"
)


# ------------------------------------------------------------
# 4.2. Supervivencia según sexo
# ------------------------------------------------------------

supervivencia_sexo = df.groupby("sex")["survived"].mean() * 100

print("\n2. Tasa de supervivencia por sexo:")
print(supervivencia_sexo)


# ------------------------------------------------------------
# 4.3. Supervivencia según clase
# ------------------------------------------------------------

supervivencia_clase = df.groupby("pclass")["survived"].mean() * 100

print("\n3. Tasa de supervivencia por clase:")
print(supervivencia_clase)


# ------------------------------------------------------------
# 4.4. Supervivencia según grupo de edad
# ------------------------------------------------------------

supervivencia_edad = df.groupby("age_group")["survived"].mean() * 100

print("\n4. Tasa de supervivencia por grupo de edad:")
print(supervivencia_edad)


# ------------------------------------------------------------
# 4.5. Grupo de edad con mayor supervivencia
# ------------------------------------------------------------

grupo_mayor_supervivencia = supervivencia_edad.idxmax()
mayor_supervivencia = supervivencia_edad.max()

print(
    f"\n5. Grupo de edad con mayor proporción de supervivientes: "
    f"{grupo_mayor_supervivencia} ({mayor_supervivencia:.2f}%)"
)


# ------------------------------------------------------------
# 4.6. Supervivencia combinando sexo y clase
# ------------------------------------------------------------

supervivencia_sexo_clase = (
    df.groupby(["sex", "pclass"])["survived"].mean() * 100
)

print("\n6. Tasa de supervivencia por sexo y clase:")
print(supervivencia_sexo_clase)


# ------------------------------------------------------------
# 4.7. Estadísticas adicionales
# ------------------------------------------------------------

print("\n7. Estadísticas adicionales:")

print(f"Número total de pasajeros: {df.shape[0]}")
print(f"Edad media: {df['age'].mean():.2f} años")
print(f"Edad mediana: {df['age'].median():.2f} años")
print(f"Tarifa media: {df['fare'].mean():.2f}")
print(f"Tarifa máxima: {df['fare'].max():.2f}")


# ------------------------------------------------------------
# 4.8. Filtros con dos condiciones
# ------------------------------------------------------------

# Mujeres de primera clase
mujeres_primera = df[
    (df["sex"] == "female") &
    (df["pclass"] == 1)
]

print(
    f"\n8. Mujeres de primera clase: "
    f"{mujeres_primera.shape[0]} pasajeros"
)


# Hombres de tercera clase que no sobrevivieron
hombres_tercera_no_sobrevivieron = df[
    (df["sex"] == "male") &
    (df["pclass"] == 3) &
    (df["survived"] == 0)
]

print(
    f"Hombres de tercera clase que no sobrevivieron: "
    f"{hombres_tercera_no_sobrevivieron.shape[0]} pasajeros"
)


# ============================================================
# T5: CONCLUSIONES
# ============================================================

print("\n" + "=" * 50)
print("T5: CONCLUSIONES")
print("=" * 50)


# ------------------------------------------------------------
# 5.1. Conclusión sobre la supervivencia general
# ------------------------------------------------------------

print(
    f"\n1. La tasa de supervivencia general fue del "
    f"{supervivencia_general:.2f}%. "
    "Esto indica que menos de la mitad de los pasajeros "
    "del dataset sobrevivieron."
)


# ------------------------------------------------------------
# 5.2. Conclusión sobre el sexo
# ------------------------------------------------------------

sexo_mayor = supervivencia_sexo.idxmax()
sexo_mayor_valor = supervivencia_sexo.max()

sexo_menor = supervivencia_sexo.idxmin()
sexo_menor_valor = supervivencia_sexo.min()

print(
    f"\n2. La tasa de supervivencia fue diferente según el sexo. "
    f"El grupo con mayor tasa fue {sexo_mayor}, con un "
    f"{sexo_mayor_valor:.2f}%, mientras que {sexo_menor} tuvo "
    f"un {sexo_menor_valor:.2f}%."
)


# ------------------------------------------------------------
# 5.3. Conclusión sobre la clase
# ------------------------------------------------------------

clase_mayor = supervivencia_clase.idxmax()
clase_mayor_valor = supervivencia_clase.max()

clase_menor = supervivencia_clase.idxmin()
clase_menor_valor = supervivencia_clase.min()

print(
    f"\n3. La clase del billete también mostró diferencias "
    f"en la supervivencia. La clase {clase_mayor} presentó "
    f"la mayor tasa de supervivencia "
    f"({clase_mayor_valor:.2f}%), mientras que la clase "
    f"{clase_menor} presentó la menor "
    f"({clase_menor_valor:.2f}%)."
)


# ------------------------------------------------------------
# 5.4. Conclusión sobre la edad
# ------------------------------------------------------------

print(
    f"\n4. Al analizar los grupos de edad, el grupo "
    f"{grupo_mayor_supervivencia} presentó la mayor proporción "
    f"de supervivientes, con un {mayor_supervivencia:.2f}%."
)


# ------------------------------------------------------------
# 5.5. Conclusión sobre sexo y clase
# ------------------------------------------------------------

combinacion_mayor = supervivencia_sexo_clase.idxmax()
valor_combinacion_mayor = supervivencia_sexo_clase.max()

print(
    f"\n5. La combinación de sexo y clase también mostró "
    f"diferencias en la supervivencia. La combinación "
    f"{combinacion_mayor[0]} de clase {combinacion_mayor[1]} "
    f"presentó una tasa de supervivencia del "
    f"{valor_combinacion_mayor:.2f}%."
)