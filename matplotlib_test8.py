# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:50:13 2017
测试pyplot文本标签的使用
@author: mav
"""

import matplotlib.pyplot  as plt
#import matplotlib as mt
import numpy as np
#mt.rcParams['font.family']="SimHei"
#mt.rcParams['font.size']=20
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),"ro-")
plt.xlabel("横轴：时间（年）",fontproperties="SimHei",fontsize=15,color='blue')
plt.ylabel("纵轴：振幅（个）",fontproperties="SimHei",fontsize=15)
plt.title(r"正弦波实例$y=cos(2\pi x)$",fontproperties="SimHei",fontsize=25)
plt.text(2,1,r'$\mu=100$',fontsize=15,color='green')
plt.annotate(2,2,r'11',fontsize=15,color='green')

plt.axis([-1,6,-2,2])#坐标范围
plt.grid(True)#加入网格曲线
plt.savefig('test8',dpi=600)
plt.show()