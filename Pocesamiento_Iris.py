# Pasos que realiza el script preprocesamiento_Iris.py

# 1. Carga del dataset Iris desde scikit-learn y lo convierte a DataFrame.

# 2. Reemplaza el target numérico por el nombre de la especie (species) para mayor legibilidad.

# 3. Renombra las columnas a formato snake_case (sepal_length, sepal_width, petal_length, petal_width).

# 4. Verifica valores nulos: informa si hay nulos; (si existieran) imputaría numéricos con la mediana y la especie con la moda.

# 5. Elimina duplicados y reporta cuántos registros se quitaron.

# 6. Codifica la variable categórica species con One-Hot Encoding (usando drop_first=True para evitar colinealidad completa).

# 7. Normaliza las columnas numéricas (sepal_length, sepal_width, petal_length, petal_width) con MinMaxScaler a rango [0, 1].

# 8. Muestra una vista previa (primeras 5 filas) del DataFrame final procesado.

# 9. Guarda el resultado en data/processed/iris_procesado.csv.

#Prueba Pull Request


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

def cargar_datos():
    """
    Carga el dataset Iris desde scikit-learn y lo devuelve como DataFrame.
    """
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()  # incluye features y 'target'
    # Reemplazo 'target' numérico por nombre de especie, más legible
    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
    df.drop(columns=["target"], inplace=True)
    print("Paso 0  Dataset Iris cargado correctamente")
    return df

def preprocesar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline MUY simple de limpieza/transformación:
    1) Renombrar columnas a un formato consistente
    2) Verificar/gestionar nulos (Iris no trae nulos, pero lo dejo explícito)
    3) Eliminar duplicados
    4) One-Hot Encoding para 'species'
    5) Normalización MinMax para variables numéricas
    """
    # 1) Renombrar columnas
    df = df.rename(columns={
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)":  "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)":  "petal_width",
    })
    print("Paso 1  Columnas renombradas a snake_case")

    # 2) Nulos (Iris no trae nulos; si hubiera, los imputaría)
    nulos = df.isna().sum().sum()
    if nulos > 0:
        # Ejemplo de imputación rápida si existieran nulos numéricos:
        num_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        for c in num_cols:
            df[c] = df[c].fillna(df[c].median())
        # Para 'species' (categórica) usaría la moda
        df["species"] = df["species"].fillna(df["species"].mode()[0])
        print(f"Paso 2  Nulos imputados (total: {nulos})")
    else:
        print("Paso 2  No hay valores nulos en Iris")

    # 3) Eliminar duplicados
    antes = len(df)
    df = df.drop_duplicates()
    eliminados = antes - len(df)
    print(f"Paso 3  Duplicados eliminados: {eliminados}")

    # 4) One-Hot Encoding para la especie (drop_first=True para evitar colinealidad total)
    df = pd.get_dummies(df, columns=["species"], drop_first=True)
    print("Paso 4  Variable 'species' codificada con One-Hot Encoding")

    # 5) Normalización MinMax de las columnas numéricas
    scaler = MinMaxScaler()
    num_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    df[num_cols] = scaler.fit_transform(df[num_cols])
    print("Paso 5  Columnas numéricas normalizadas (Min-Max)")

    print("\n--- PREPROCESAMIENTO COMPLETADO ---")
    return df

def guardar_datos(df: pd.DataFrame, nombre_archivo: str):
    """
    Guarda el DataFrame procesado en CSV.
    """
    df.to_csv(nombre_archivo, index=False)
    print(f"\nDataset limpio guardado exitosamente como '{nombre_archivo}'")

# --- Flujo Principal ---
if __name__ == "__main__":
    # 1) Cargar
    datos_originales = cargar_datos()

    # 2) Preprocesar
    datos_procesados = preprocesar_datos(datos_originales)

    # 3) Vista previa
    print("\nPrimeras 5 filas del dataset final:")
    print(datos_procesados.head())

    # 4) Guardar
    guardar_datos(datos_procesados, "data/processed/iris_procesado.csv")
