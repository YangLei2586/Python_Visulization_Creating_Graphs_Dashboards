Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part Five Draw Waveform
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x=np.linspace(0,10,1200)
>>> y=np.sin(x)+1
>>> z=np.cos(x**2)+1
>>> # Setting size
>>> plt.Figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
>>> plt.plot(x,y,label='$\cosx+1$',color="red",linewidth=2)
[<matplotlib.lines.Line2D object at 0x00E19930>]
>>> plt.plot(x,z,label='$\cos x^2+1$')
[<matplotlib.lines.Line2D object at 0x00E19C10>]
>>> # setting x-axis
>>> plt.xlabel("Time(s)")
Text(0.5, 0, 'Time(s)')
>>> plt.ylabel("volt")
Text(0, 0.5, 'volt')
>>> plt.title("waveform")
Text(0.5, 1.0, 'waveform')
>>> plt.ylim(0,2)
(0, 2)
>>> plt.legend()
<matplotlib.legend.Legend object at 0x00E0D430>
>>> plt.savefig("5.png",dpi=120)
>>> plt.show()
>>> 
