import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



x = [1,2,3,4,5,3.5,6,6.5] # x 轴的坐标
y = [n*2 + 1 for n in x]  # y轴的坐标
plt.plot(x, y, color='red', linewidth=2)
plt.scatter(x, y, color='blue')
plt.xlabel("x")
plt.ylabel('y')

plt.savefig('1.png')
plt.show()