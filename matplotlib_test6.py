# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:37:45 2017

@author: mav
"""

import matplotlib.pyplot  as plt
import matplotlib as mt
mt.rcParams['font.family']="SimHei"
mt.rcParams['font.size']=20
plt.plot([3,4,5,2,1,5])
plt.ylabel("纵轴（年）")
plt.title("名义GDP")
plt.savefig('test6',dpi=600)
plt.show()