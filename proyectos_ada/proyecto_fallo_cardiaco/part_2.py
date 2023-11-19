from datasets import load_dataset
import pandas as pd

# se accede al dataset
dataset = load_dataset("mstz/heart_failure")
# se accede a train y se guada como data
data = dataset["train"]
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