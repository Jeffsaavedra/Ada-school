from datasets import load_dataset
from main import descargar_y_guardar_csv, limpieza_preparacion_datos
import numpy as np
import pandas as pd

# ------------>>>>>>>>>>>> PARTE 6 <<<<<<<<<<<<------------

#------>>>>>>>>  Uso e implementación parte 1
#* Se carga el conjunto de datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#* Acceder a la característica 'age' y convertirla a un arreglo de NumPy
ages = np.array(data['age'])
has_anemia = np.array(data['has_anaemia'])

#* Calcular el promedio de edad
average_age = np.mean(ages)
#* Calcular las personas con anemia
sum_has_anemia = np.sum(has_anemia)

# TODO: print(has_anemia) 
# TODO: print(data)
# TODO: print(ages)
print(f"\n{sum_has_anemia} personas tienen anemia.")
print(f"El promedio de edad de las personas participantes en el estudio es: {average_age:.2f}\n" )


#------>>>>>>>>  Uso e implementación parte 2
#* Convertir el Dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

dead_df = df[df['is_dead'] == 1]
survived_df = df[df['is_dead'] == 0]

av_age_dead = dead_df['age'].mean()
av_age_survived = survived_df['age'].mean()

print(f"Promedio de edad de personas que perecieron: {av_age_dead:.2f}")
print(f"Promedio de edad de personas que sobrevivieron: {av_age_survived:.2f}")

#------>>>>>>>> Uso e implementación Parte 3
smoker_counts = df.groupby(['is_male', 'is_smoker']).size().unstack()

# Cambiar nombres de las columnas
smoker_counts.columns = ['No Fumador', 'Fumador']
# Cambiar nombres de los índices(Filas)
smoker_counts.index = ['Mujer', 'Hombre']

print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(f"{smoker_counts}\n")

#------>>>>>>>> Uso e implementación parte 4
url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'


descargar_y_guardar_csv(url, 'datos5.csv')

df = pd.read_csv('datos5.csv')
df_cleaned = limpieza_preparacion_datos(df)