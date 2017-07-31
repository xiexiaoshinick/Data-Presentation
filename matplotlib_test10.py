# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:31:30 2017
实现多区域绘图（辅助subplot绘图的方法plt.subplot2grid()）
@author: mav
"""

import matplotlib.pyplot  as plt
import matplotlib.gridspec as gridespec
gs = gridespec.GridSpec(3,3)#规定一个确定的区域。
#import matplotlib as mt
import numpy as np
a = np.arange(0.0,5.0,0.02)
b = np.arange(0.0,10.0,0.04)
c = np.arange(0.0,10.0,0.04)
d = np.arange(0.0,10.0,0.04)
d = np.arange(0.0,5.0,0.02)
#plt.subplot2grid((3,3),(0,0),colspan=3)
ax1 =plt.subplot(gs[0,:])
plt.plot(a,np.cos(2*np.pi*a),"ro-")
#plt.show()
ax1 =plt.subplot(gs[1,:-1])
#plt.subplot2grid((3,3),(1,0),colspan=2)
plt.plot(a,np.sin(2*np.pi*a),"r*-")
#plt.show()
#plt.subplot2grid((3,3),(1,2),rowspan=2)
ax1 =plt.subplot(gs[1:,-1])
plt.plot(a,np.tan(2*np.pi*a),"y*-")
#plt.show()
ax1 =plt.subplot(gs[2,0])
#plt.subplot2grid((3,3),(2,0),colspan=1)
plt.plot(a,np.cosh(2*np.pi*a),"g*-")
#plt.show()
#plt.subplot2grid((3,3),(2,1),colspan=1)
ax1 =plt.subplot(gs[2,1])
plt.plot(a,np.sinh(2*np.pi*a),"b*-")
plt.show() 
#plt.subplot2grid((3,3),(2,2))
#plt.plot(a,np.tanh(2*np.pi*a),"y*-")
#plt.show() 