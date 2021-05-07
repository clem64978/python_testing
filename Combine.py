import pandas as pd
import numpy as np
import glob


all_data = pd.DataFrame()
df = pd.read_excel("datasets/data1.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("datasets/data2.xlsx")
all_data = all_data.append(df,ignore_index=True)
df = pd.read_excel("datasets/data3.xlsx")
all_data = all_data.append(df,ignore_index=True)
all_data.describe()



# Short Way
all_data = pd.DataFrame()
for f in glob.glob("datasets/data*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()



