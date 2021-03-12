#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)


plt.suptitle('All in One')
plt.subplots_adjust(wspace=0.8, hspace=1)


plt.rc('axes', titlesize='x-small')
plt.rc('axes', labelsize='x-small')
plt.rc('legend', fontsize='x-small')

ax1 = plt.subplot(321)
ax1.set_xlim(0, 10)
ax1.set_yticks(np.arange(0, 1500, step=500))
ax1.plot(y0, color='red')

ax2 = plt.subplot(322)
ax2.set_xlabel('Height (in)')
ax2.set_ylabel('Weight (lbs)')
ax2.set_title('Men\'s Height vs Weight')
ax2.scatter(x1, y1, s=7, c='m')


ax3 = plt.subplot(323)
ax3.set_xlabel('Time (years)')
ax3.set_ylabel('Fraction Remaining')
ax3.set_title('Exponential Decay of C-14')
ax3.set_yscale('log')
ax3.set_xlim(0, 2800)
ax3.plot(x2, y2)

ax4 = plt.subplot(324)
ax4.set_xlabel('Time (years)')
ax4.set_ylabel('Fraction Remaining')
ax4.set_title('Exponential Decay of Radioactive Elements')
ax4.set_xlim(0, 20000)
ax4.set_ylim(0, 1)
line1 = plt.plot(x3, y31, 'r--', label='C-14')
line2 = plt.plot(x3, y32, 'g-', label='Ra-226')
ax4.legend()

axbig = plt.subplot(313)
axbig.set_xlabel('Grades')
axbig.set_ylabel('Number of Students')
axbig.set_title('Project A')
axbig.hist(student_grades, bins=10, range=(0, 100), edgecolor='black')
axbig.set_xlim(0, 100)
axbig.set_ylim(0, 30)
axbig.set_xticks(np.arange(0, 110, step=10))


plt.show()
