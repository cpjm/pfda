import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0,10.0,0.01)
y = 3.0 * x
noise=np.random.normal(0.0,2,len(x))
###plt.plot([1,2,3,4])
###plt.ylabel('some numbers')
###plt.show()

#drawing 2 lines on a graph
plt.plot(x,y+noise,'g-')
plt.plot(x,y,'b.')
plt.ylabel('some numbers')
plt.show()
