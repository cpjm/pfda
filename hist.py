import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0,1.0,10000)
#plt.plot(x)

#subplot - one row, 2 columns, use first column
plt.subplot(1,2,1)
plt.hist(x, bins=80)

x = np.random.uniform(-4.0,3.0,10000)
#subplot - one row, 2 columns, use second column
plt.subplot(1,2,2)
plt.hist(x)

plt.show()

