import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

reader = csv.reader(open("PM25/PM25/PMB_6.csv", "rt"))
x = list(reader)
result = np.array(x).astype("float")


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.linspace(0, 1, num=121)
Y = np.linspace(0, 1, num=365)
X, Y = np.meshgrid(X, Y)
Z = result


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.5, 1.5)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
fig.savefig('PMB_6.png')


