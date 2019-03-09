Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part One Draw a simple Line
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x=np.arange(0,16,1)
>>> y=x+10
>>> plt.plot(x,y,color="red",linestyle="--",marker="*",label='y=x+8')
[<matplotlib.lines.Line2D object at 0x011743F0>]
>>> plt.savefig("1.png",dpi=60)
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0306B7F0>
>>> plt.show()
>>> 
