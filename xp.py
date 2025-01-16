import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/costs-c3po-202302-202402.csv')

print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
# 1. treat AWS input data

#1.1
