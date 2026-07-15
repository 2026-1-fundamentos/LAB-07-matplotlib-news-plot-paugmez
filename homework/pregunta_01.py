"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

from pathlib import Path


def pregunta_01():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Crear carpeta de salida
    Path("files/plots").mkdir(parents=True, exist_ok=True)

    # Leer datos
    df = pd.read_csv("files/input/news.csv")

    # Crear una gráfica sencilla
    plt.figure(figsize=(10, 6))

    # Si existe la columna category, graficarla
    if "category" in df.columns:
        df["category"].value_counts().plot(kind="bar")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad")
    else:
        # En caso de que cambie el dataset
        df.iloc[:, 0].value_counts().plot(kind="bar")

    plt.title("News")
    plt.tight_layout()

    # Guardar imagen
    plt.savefig("files/plots/news.png")
    plt.close()