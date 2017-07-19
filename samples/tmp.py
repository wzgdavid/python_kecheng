
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 画一个5 5 的矩阵
cm = np.random.randint(9, size=(4,4))
plt.imshow(cm, cmap = plt.cm.Reds) 
plt.show()