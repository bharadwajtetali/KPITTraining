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

f,ax = plt.subplots(3, sharex= True)
ax[0].set_title('Graph which represents Light, Sound and Acceleration')
ax[0].plot(light)
ax[0].set_ylabel("Lux")
ax[1].plot(sound)
ax[1].set_ylabel("dB")
ax[2].plot(speed)
ax[2].set_ylabel("m/s2")
plt.xlabel('Time in ms')

plt.show()


