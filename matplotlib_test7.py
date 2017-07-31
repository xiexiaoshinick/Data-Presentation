# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:27:28 2017

@author: mav
"""

import matplotlib.pyplot  as plt
import matplotlib as mt
import numpy as np
#mt.rcParams['font.family']="SimHei"
#mt.rcParams['font.size']=20
a = np.arange(0.0,5.0,0.02)
plt.xlabel("时间（年）",fontproperties="SimHei",fontsize=20)
plt.ylabel("纵轴（个）",fontproperties="SimHei",fontsize=20)
plt.title("名义GDP",fontproperties="SimHei",fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),"ro-")
plt.savefig('test7',dpi=600)
plt.show()