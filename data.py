import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub
import mlflow

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

with mlflow.experiment("Sephora"):

# Download latest version
path = kagglehub.dataset_download("raghadalharbi/all-products-available-on-sephora-website")

print("Path to dataset files:", path)

data = os.listdir(path)

df = pd.read_csv(os.path.join(path, data[0]))
df.to_csv("data/raw"+ "/" + data[0], index=False)
print(df.head())

