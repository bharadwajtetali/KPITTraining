import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("androsense.csv",sep=",")
df.set_index('Time', inplace=True)

rows = df.shape[0]
cols= df.shape[1]

light = df.iloc[:, 9]
sound = df.iloc[:, 10]
speed = df.iloc[:,2]
avg_sound = sound.mean()
max_sound = sound.max()
avg_light = light.mean()
max_speed = speed.max()
avg_speed = speed.mean()

print("Average Light: ",avg_light)
print("Average Sound: ",avg_sound)
print("Maximum Sound: ",max_sound)
print("Maximum Speed: ",max_speed)
print("Average Speed: ",avg_speed)

def plt_light(df):
    plt.plot(df.iloc[: 9])

def plt_sound(df):
    plt.plot(df.iloc[:10])


#print(a1.shape)
#print(df)
df.plot()
plt.show()



#def column(mtx,idx):
    #ret=[]
   # for i in range(0,len(mtx)):
  #      ret.append(mtx[i][idx])
 #   return ret

