import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0,10.0,0.01)
y = 3.0 * x
noise=np.random.normal(0.0,2,len(x))
###plt.plot([1,2,3,4])
###plt.ylabel('some numbers')
###plt.show()

#drawing 2 lines on a graph
plt.plot(x,y+noise,'g.',label='Actual data')
plt.plot(x,y,'b-',label='Fitted model')
plt.ylabel('some numbers')

plt.title("Average speed vs. Distance covered over time")
plt.xlabel("Average speed (km/h))")
plt.ylabel("Distance covered over time (km)")
plt.legend()

plt.show()

