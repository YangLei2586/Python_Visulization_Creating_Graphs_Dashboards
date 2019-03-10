Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part Four Draw Histgram
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x=np.random.randint(1,800,300)
>>> axit=plt.gca()
>>> axit.hist(x,bins=35,facecolor='r',
	      normed=True,histtype="bar",
	      alpha=0.5)

Warning (from warnings module):
  File "C:\Users\LylionCj\AppData\Local\Programs\Python\Python36-32\lib\site-packages\matplotlib\axes\_axes.py", line 6521
    alternative="'density'", removal="3.1")
MatplotlibDeprecationWarning: 
The 'normed' kwarg was deprecated in Matplotlib 2.1 and will be removed in 3.1. Use 'density' instead.
(array([0.00087829, 0.00131744, 0.00102468, 0.00117106, 0.00190297,
       0.00102468, 0.00175659, 0.00146382, 0.00219573, 0.00131744,
       0.00117106, 0.00146382, 0.00131744, 0.00102468, 0.00131744,
       0.00146382, 0.00073191, 0.00102468, 0.0016102 , 0.00102468,
       0.00131744, 0.00117106, 0.00117106, 0.00073191, 0.00190297,
       0.0016102 , 0.00058553, 0.00087829, 0.00087829, 0.00131744,
       0.00087829, 0.00102468, 0.00175659, 0.0016102 , 0.00087829]), array([  2.        ,  24.77142857,  47.54285714,  70.31428571,
        93.08571429, 115.85714286, 138.62857143, 161.4       ,
       184.17142857, 206.94285714, 229.71428571, 252.48571429,
       275.25714286, 298.02857143, 320.8       , 343.57142857,
       366.34285714, 389.11428571, 411.88571429, 434.65714286,
       457.42857143, 480.2       , 502.97142857, 525.74285714,
       548.51428571, 571.28571429, 594.05714286, 616.82857143,
       639.6       , 662.37142857, 685.14285714, 707.91428571,
       730.68571429, 753.45714286, 776.22857143, 799.        ]), <a list of 35 Patch objects>)
>>> axit.set_xlabel("values")
Text(0.5, 0, 'values')
>>> axit.set_title("Histgram")
Text(0.5, 1.0, 'Histgram')
>>> plt.savefig("4.png",dpi=150)
>>> plt.show()
>>> 
