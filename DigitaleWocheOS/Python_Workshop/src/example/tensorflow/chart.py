import matplotlib.pyplot as plt
import numpy as np

x = 0.5 + np.arange(8)
y = [0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8]

fig, ax = plt.subplots()
ax.bar(x, y, width = 1, edgecolor = "white", linewidth=0.7)
ax.set(xlim=(0, 8), xticks=np.arange(1,8),
       ylim=(0, 13), yticks=np.arange(1,13))
plt.show()