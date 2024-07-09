import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df1=pd.read_csv(r"C:\Users\amber\Desktop\空调\process_lixiang_63a1604134e2990a96ad5259.csv",usecols=['set_tp_Z01','return_tp_Z01','power_Z01'])
print(df1.head())