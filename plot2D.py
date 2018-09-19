import matplotlib.pyplot as plt
import numpy as np
import csv

# read in data
reader = csv.reader(open("PM25/PM25/PMB_6.csv", "rt"))
x = list(reader)
result = np.array(x).astype("float")


# Make data.
X = np.linspace(0, 1, num=121)
Y = np.linspace(0, 1, num=365)
X, Y = np.meshgrid(X, Y)
Z = result

fig = plt.figure()
# coloring the contour regions and set up the total number of value level
C1 = plt.contourf(X, Y, Z, 22, alpha=1, cmap=plt.cm.coolwarm)
plt.colorbar(C1)
# plot the contour
#C = plt.contour(X, Y, Z, 12, colors ='black', linewidth = 0.5)
# add the value of each contour line
#plt.clabel(C, inline = True, fontsize = 10)

# Get rid of the axes
#plt.xticks(())
#plt.yticks(())
plt.show()
fig.savefig("PMB_6.png")