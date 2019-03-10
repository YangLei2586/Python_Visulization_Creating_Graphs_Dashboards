Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part Three Draw Scatter Plot
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x=np.random.rand(1000)
>>> y=np.random.rand(len(x))
>>> 
>>> # drawing
>>> plt.scatter(x,y,color='b',label="scatter plot",
	        alpha=0.3,marker="p")
<matplotlib.collections.PathCollection object at 0x0111D4D0>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x01114E30>
>>> plt.savefig("3.png",dpi=60)
>>> plt.show()
>>> 
