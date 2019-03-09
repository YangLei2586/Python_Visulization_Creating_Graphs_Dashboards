Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Part Two Draw a Pie Chart
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> # specify proportion
>>> sclice = [2,3,6,8]
>>> # label
>>> activity = ["sleep","eating","study","work"]
>>> # color
>>> color = ['b','m','r','w']
>>> 
>>> plt.pie(sclice,labels=activity,
	    colors=color,
	    startangle=0,
	    shadow=True,
	    explode=(0,0.2,0,0),
	    autopct='%1.1f%%')
([<matplotlib.patches.Wedge object at 0x00A14530>, <matplotlib.patches.Wedge object at 0x00A14AB0>, <matplotlib.patches.Wedge object at 0x00A26050>, <matplotlib.patches.Wedge object at 0x00A26610>], [Text(1.0403989649906822, 0.3571694186885514, 'sleep'), Text(0.5222040696483053, 1.1905053169317423, 'eating'), Text(-0.9674210876290679, 0.5235422038485451, 'study'), Text(0.27003392550763244, -1.0663403204769752, 'work')], [Text(0.567490344540372, 0.194819682921028, '10.5%'), Text(0.3213563505528033, 0.7326186565733797, '15.8%'), Text(-0.5276842296158551, 0.2855684748264791, '31.6%'), Text(0.14729123209507222, -0.5816401748056228, '42.1%')])
>>> plt.title("activity analysis")
Text(0.5, 1.0, 'activity analysis')
>>> plt.savefig("2.png")
>>> plt.show()
>>> 
