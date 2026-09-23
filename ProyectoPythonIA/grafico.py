import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# T1: CARGA E INSPECCIÓN INICIAL
print("--- T1: CARGA E INSPECCIÓN ---")

# 1. Cargar el dataset directamente
df = sns.load_dataset("titanic")

# 2. Inspección del contenido
print("\n🔹 Primeras filas del dataset (.head()):")
print(df.head())

print("\n🔹 Información general y tipos de datos (.info()):")
df.info()

print("\n🔹 Estadísticas descriptivas de columnas numéricas (.describe()):")
print(df.describe())

print(f"\n🔹 Forma del dataset (Filas, Columnas): {df.shape}")


