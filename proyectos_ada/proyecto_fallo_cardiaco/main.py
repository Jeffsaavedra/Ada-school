
# ------------>>>>>>>>>>>> PARTE 1  <<<<<<<<<<<<------------

from datasets import load_dataset
import numpy as np

# Descargar el conjunto de datos
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición de entrenamiento
data = dataset["train"]

# Convertir la lista de edades a un arreglo de NumPy
edades = np.array(data["age"])

# Calcular el promedio de edad
media_edad = np.mean(edades)

# Imprimir el resultado
print("El promedio de la edad de los participantes de este estudio es :", media_edad, "años")

# ------------>>>>>>>>>>>> PARTE 2  <<<<<<<<<<<<------------

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

# ------------>>>>>>>>>>>> PARTE 3  <<<<<<<<<<<<------------

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

# ------------>>>>>>>>>>>> PARTE 4  <<<<<<<<<<<<------------

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

# ------------>>>>>>>>>>>> PARTE 5 <<<<<<<<<<<<------------


def limpieza_preparacion_datos(df : pd.DataFrame):
  
  # Verificar valores faltantes
  if df.isnull().any().any():
    print("Hay valores faltantes en el DataFrame. Realiza la imputación o eliminación según sea necesario.")
    # Correcciones para valores faltantes.
    df = df.fillna(df.mean()) #  se le asigna el valor de la media de cada columna a los valores faltantes.
  else:
    print("No hay valores faltantes en el DataFrame.")
    
  # verificar filas repetidas
  if df.duplicated().any():
    print("Hay valores duplicados en el DataFrame. se relizarán las correcciones necesarias")
    # correcciones necesarias para eliminar duplicados
    df = df.drop_duplicates() # en este caso no se indica el keep ya que queremos conservar el primero (predeterminado)
  else:
    print("No hay valores repetidos en el DataFrame.")  

  # ELiminar valores atipicos
  Q1 = df.quantile(0.25)  # Hayamos primer cuartil para cada columna
  Q3 = df.quantile(0.75)  # Hayamos tercer cuartil para cada columna

  IQR = Q3 - Q1   # Hayamos rango intercuartil para cada columna

  limite_min = Q1 - (1.5 * IQR) # Hallamos el límite mínimo de la desviación estandar
  limite_max = Q3 + (1.5 * IQR) # Hallamos el límite máximo de la desviación estandar

    # Filtramos los valores atípicos
  df = df[(df >= limite_min) & (df <= limite_max)]

  # Creamos columna para clasificar por edades
  df['categoria_edad'] = pd.cut(df['age'],
                                  bins=[-float("inf"), 12, 19, 39, 59, float('inf')],
                                  labels=['Niño', 'Adolescente', 'Joven adulto', 'Adulto', 'Adulto mayor'],
                                  right=True
                                  )
    # Guardar el resultado como CSV
  df.to_csv("datos_corregidos.csv", index=False)
  print("Datos limpios y preparados guardados como 'datos_corregidos.csv'.")

df = pd.read_csv("datos_descargados.csv")

limpieza_preparacion_datos(df)

# ------------>>>>>>>>>>>> PARTE 11 <<<<<<<<<<<<------------

import pandas as pd
from clasificacion import graficar_distribucion_clases, particion_estratificada, ajustar_arbol_decision

# Cargar el DataFrame con los datos procesados
df = pd.read_csv('datos_procesados.csv')

# Utilizar las funciones de clasificación
graficar_distribucion_clases(df)
X_train, X_test, y_train, y_test = particion_estratificada(df)
ajustar_arbol_decision(X_train, X_test, y_train, y_test)
