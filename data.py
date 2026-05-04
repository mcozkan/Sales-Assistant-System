from os.path import exists

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import kagglehub
import mlflow

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

mlflow.set_experiment("CosmeticAssistant")

with mlflow.start_run("data_load"):

    # Download latest version
    path = kagglehub.dataset_download("raghadalharbi/all-products-available-on-sephora-website")

    data = os.listdir(path)
    data_full_path = os.path.join(path, data[0])

    df = pd.read_csv(data_full_path)
    target_path = os.mkdir("data/raw", exist_ok = True)

    df.to_csv("data/raw"+ "/" + data[0], index=False)
    print(df.head())

