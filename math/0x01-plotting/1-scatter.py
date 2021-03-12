#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.ylabel('Weight (lbs)')
plt.xlabel('Height (in)')
plt.title('Men\'s Height vs Weight')

plt.scatter(x, y, s=9, c='m')
plt.show()
