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
df1 = df.query("is_dead == 1")
df2 = df.query("is_dead == 0")

# se calculan los promedios de edad por dataset y se imprime
media_df1 = df1["age"].mean()
print(media_df1)
media_df2 = df2["age"].mean()
print(media_df2)

