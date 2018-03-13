import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import csv file to a dataframe as df using pandas
df = pd.read_csv("androsense.csv",sep=",")
#Setting Time column as index
df.set_index('Time', inplace=True)

#Storing light, sound, acceleration column in an array. Using iloc() to find the location of the column
light = df.iloc[:, 9]
sound = df.iloc[:, 10]
accel = df.iloc[:,2]

#Calculating the features
avg_sound = sound.mean()
max_sound = sound.max()
avg_light = light.mean()
max_accel = accel.max()
avg_accel = accel.mean()

print("Average Light in Lux: ",avg_light)
print("Average Sound in dB: ",avg_sound)
print("Maximum Sound in dB: ",max_sound)
print("Maximum Acceleration in m/s2: ",max_accel)
print("Average Acceleration in m/s2: ",avg_accel)

#Plotting the graph with the help of subplots in matplotlib
#Sharing the same X-axis as Time with all 3 graphs
f,ax = plt.subplots(3, sharex = True)
ax[0].set_title('Graph which represents Light, Sound and Acceleration')
ax[0].plot(light)
ax[0].set_ylabel("Lux")
ax[1].plot(sound)
ax[1].set_ylabel("dB")
ax[2].plot(accel)
ax[2].set_ylabel("m/s2")
plt.xlabel('Time in ms')

plt.show()


