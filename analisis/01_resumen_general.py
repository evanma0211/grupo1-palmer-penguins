"""Parte 1 - Resumen general del dataset Palmer Penguins.

Autora: Yifan Ma (@evanma0211)

Calcula el tamaño del dataset, los valores faltantes, los estadísticos
básicos de las variables numéricas y los valores más frecuentes de las
variables categóricas. Guarda dos figuras en `figuras/`.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "data" / "penguins.csv"
FIGURAS = RAIZ / "figuras"
FIGURAS.mkdir(exist_ok=True)

df = pd.read_csv(DATOS)

# 1. Tamaño del dataset
print(f"Filas: {df.shape[0]}  |  Columnas: {df.shape[1]}")
print("Columnas:", ", ".join(df.columns))

# 2. Valores faltantes por columna
faltantes = df.isna().sum()
print("\nValores faltantes por columna:")
print(faltantes.to_string())

# 3. Estadísticos básicos de las variables numéricas
numericas = df.select_dtypes("number")
print("\nEstadísticos de las variables numéricas:")
print(numericas.describe().round(1).to_string())

# 4. Valor más frecuente de las variables categóricas
print("\nValor más frecuente de las variables categóricas:")
for col in df.select_dtypes(exclude="number").columns:
    moda = df[col].mode()[0]
    n = (df[col] == moda).sum()
    print(f"  {col}: {moda} ({n} de {df[col].notna().sum()})")

# Figura 1: valores faltantes por columna
fig, ax = plt.subplots(figsize=(6, 3.2))
faltantes.plot.barh(ax=ax, color="#4C72B0")
ax.set_xlabel("Número de valores faltantes")
ax.set_title("Valores faltantes por columna")
for i, v in enumerate(faltantes):
    ax.text(v + 0.1, i, str(v), va="center", fontsize=8)
fig.tight_layout()
fig.savefig(FIGURAS / "01_valores_faltantes.png", dpi=110)

# Figura 2: histogramas de las variables numéricas
nombres = {
    "bill_length_mm": "Longitud del pico (mm)",
    "bill_depth_mm": "Profundidad del pico (mm)",
    "flipper_length_mm": "Longitud de la aleta (mm)",
    "body_mass_g": "Masa corporal (g)",
}
fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))
for ax, (col, etiqueta) in zip(axes.flat, nombres.items()):
    ax.hist(df[col].dropna(), bins=20, color="#4C72B0", edgecolor="white")
    ax.set_title(etiqueta, fontsize=10)
    ax.set_ylabel("Frecuencia")
fig.suptitle("Distribución de las variables numéricas (n = 342 con datos)")
fig.tight_layout()
fig.savefig(FIGURAS / "01_histogramas.png", dpi=110)

print("\nFiguras guardadas en", FIGURAS)
