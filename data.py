import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from transformers import pipeline

pipe = pipeline("text-classification", model="ProsusAI/finbert")

import kagglehub

# Download latest version
path = kagglehub.dataset_download("raghadalharbi/all-products-available-on-sephora-website")

print("Path to dataset files:", path)
print(pipe)