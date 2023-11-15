from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")

data = dataset["train"]

edades = np.array(data["age"])

media_edad = np.mean(edades)
print("El promedio de la edad de los participantes de este estudio es :", media_edad, "años")