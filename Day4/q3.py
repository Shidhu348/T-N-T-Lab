import pandas as pd

data_set = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv")

data_set_1 = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv")

data_set_1.dropna(axis=0, inplace=True)
