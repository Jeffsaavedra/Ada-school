from datasets import load_dataset
import numpy as np

# PARTE 1

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edades = np.array(data["age"])

media_edad = np.mean(edades)
print("El promedio de la edad de los participantes de este estudio es :", media_edad, "años")

# PARTE 2

import pandas as pd

# se accede al dataset
  # dataset = load_dataset("mstz/heart_failure") YA SE HIZO ARRIBA
# se accede a train y se guada como data
  # data = dataset["train"] YA SE HIZO ARRIBA IGUAL
# se convierte la info obtenida en un dataframe
df = pd.DataFrame(data)

# se usa querry para indexar y filtrar por condición y se guarda en una nueva variable
df1 = df.query("is_dead == True")
print(df1.shape[0])
df2 = df.query("is_dead == False")
print(df2.shape[0])

# Se calculan los promedios de edad por dataset y se imprime
media_df1 = df1["age"].mean()
print("Promedio de edad de personas fallecidas:", round(media_df1, 2), "años")
media_df2 = df2["age"].mean()
print("Promedio de edad de personas no fallecidas:", round(media_df2, 2), "años")

# PARTE 3

# se muestra los tipos de cada columna con dtypes
print(df.dtypes)
# se modifican los que deban modificarse en este caso is_dead debe ser boleano y es int
df['is_dead'] = df['is_dead'].astype(bool)
# se comprueba que los tipos sean los indicados
print(df.dtypes)
print(df["is_dead"].head())

# Agrupa por género y fumador/no fumador
df_agrupado = df.groupby(['is_male', 'is_smoker']).size().reset_index(name='count')

# Imprime la agrupación para visualización
print(df_agrupado)

# Filtra los resultados para obtener las cantidades de hombres y mujeres fumadores
conteo_fumadoras = df_agrupado.loc[(df_agrupado['is_male'] == False) & (df_agrupado['is_smoker'] == True), 'count'].values
conteo_fumadores = df_agrupado.loc[(df_agrupado['is_male'] == True) & (df_agrupado['is_smoker'] == True), 'count'].values

# Imprime los resultados
print("Cantidad de mujeres fumadoras:", conteo_fumadoras[0] if len(conteo_fumadoras) > 0 else 0)
print("Cantidad de hombres fumadores:", conteo_fumadores[0] if len(conteo_fumadores) > 0 else 0)

# PARTE 4

import requests

def descargar_y_guardar_csv(url, nombre_archivo):
    # Hacer la solicitud GET
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Guardar la respuesta como un archivo CSV
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(response.text)
        print(f"Datos descargados y guardados en {nombre_archivo}")
    else:
        print(f"Error en la solicitud: {response.status_code}")

# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Llamar a la función para descargar y guardar los datos en un archivo CSV
descargar_y_guardar_csv(url_datos, "datos_descargados.csv")
