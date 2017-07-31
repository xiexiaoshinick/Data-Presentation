# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 11:04:35 2017
面向对象的绘制散点图
@author: mav
"""



import matplotlib.pyplot  as plt
import matplotlib.gridspec as gridespec
gs = gridespec.GridSpec(3,3)#规定一个确定的区域。
#import matplotlib as mt
import numpy as np
fig,ax =plt.subplots()#面向对象
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'ro')
ax.set_title('simple scatter')
plt.show() 
