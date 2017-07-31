# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:31:30 2017
实现饼图的绘制
@author: mav
"""

import matplotlib.pyplot  as plt
import matplotlib.gridspec as gridespec
gs = gridespec.GridSpec(3,3)#规定一个确定的区域。
#import matplotlib as mt
import numpy as np
labels = "froges",'dogs','hogs',"logs"
sizes  =[10,30,45,15]
expor  =[0.2,0,0.1,0]
#plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=True,startangle=90)
#   autopcts 表示中间显示百分数的方式。
plt.axis("equal")
plt.show() 
