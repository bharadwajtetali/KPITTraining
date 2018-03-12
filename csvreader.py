import csv
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
sub1 = plt.subplot(2, 2, 1)

x=[]
y=[]

with open('androaccel.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))


sub2 = plt.subplot(2, 2, 2)

x1=[]
y1=[]

with open('androaccel.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[2]))
        y1.append(float(row[2]))


plt.plot(x,y, label='Loaded from file!')
plt.xlabel('Accelerometer X axis')
plt.ylabel('Accelerometer Y axis')
plt.title('Interesting Graph')
plt.legend()
plt.show()