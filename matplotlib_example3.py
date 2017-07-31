# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:27:52 2017
实现matplotlib的极坐标图的绘制
@author: mav
"""

import matplotlib.pyplot  as plt
import matplotlib.gridspec as gridespec
gs = gridespec.GridSpec(3,3)#规定一个确定的区域。
#import matplotlib as mt
import numpy as np
np.random.seed(0)
mu,sigma=100,20 #均值和标准差
a = np.random.normal(mu,sigma,size=100)
print(a)
#labels = "froges",'dogs','hogs',"logs"
#sizes  =[10,30,45,15]
#expor  =[0.2,0,0.1,0]
#plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
#plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=True,startangle=90)
#   autopcts 表示中间显示百分数的方式。
plt.hist(a,40,normed=1,histtype='stepfilled',facecolor='b',alpha=0.75)
#plt.axis("equal")
plt.title('test')
plt.show() 