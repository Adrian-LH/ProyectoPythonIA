import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# T1: CARGA E INSPECCIÓN INICIAL
print("T1: CARGA E INSPECCIÓN")

# 1. Cargar el dataset directamente
df = sns.load_dataset("titanic")

# 2. Inspección del contenido
print("Primeras filas del dataset (.head()):")
print(df.head())

print("Información general y tipos de datos (.info()):")
df.info()

print("Estadísticas descriptivas de columnas numéricas (.describe()):")
print(df.describe())

print(f"Forma del dataset (Filas, Columnas): {df.shape}")


print("\n" + "=" * 50)
print("T2: LIMPIEZA DE DATOS (NULOS Y DUPLICADOS)")
print("=" * 50)

# 1. Filas duplicadas
duplicados = df.duplicated().sum()
print(f"Filas duplicadas encontradas: {duplicados}")

#Eliminamos las filas repetidas para no sesgar las estadísticas
df = df.drop_duplicates().reset_index(drop=True)
print(f"Filas tras eliminar duplicados: {df.shape[0]}")

# 2. Detección de nulos iniciales
print("\nValores nulos por columna antes de limpiar:")
print(df.isna().sum()[df.isna().sum() > 0])

# 3. Tratamiento de nulos y justificación:
# Faltan más del 70% de datos; se elimina para no inventar información
if "deck" in df.columns:
  df = df.drop(columns=["deck"])
  print("\n-> Columna 'deck' eliminada por exceso de valores nulos (>70%).")

# Es una variable clave. Rellenamos huecos con la mediana
# para que los valores extremos no alteren la distribución
mediana_edad = df["age"].median()
df["age"] = df["age"].fillna(mediana_edad)
print(f"-> Nulos en 'age' rellenados con la mediana: {mediana_edad:.1f} años.")

# Faltan muy pocos valores. Se rellenan con la moda (el valor más común)
moda_town = df["embark_town"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(moda_town)

moda_embarked = df["embarked"].mode()[0]
df["embarked"] = df["embarked"].fillna(moda_embarked)
print(
    f"-> Nulos en puerto de embarque rellenados con la moda: '{moda_town}' ('{moda_embarked}')."
)

# 4. Comprobación final
print("\nComprobación de nulos tras la limpieza:")
print(df.isna().sum())
print(f"Dimensiones finales del dataset limpio: {df.shape}")

