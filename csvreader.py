import csv
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("androaccel.csv",sep=",")
df.set_index('Time', inplace=True)



df.plot()
plt.show()
