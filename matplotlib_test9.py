# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:12:41 2017
实现多区域绘图（辅助subplot绘图的方法plt.subplot2grid()）
@author: mav
"""
import matplotlib.pyplot  as plt
#import matplotlib as mt
import numpy as np
a = np.arange(0.0,5.0,0.02)
b = np.arange(0.0,10.0,0.04)
c = np.arange(0.0,10.0,0.04)
d = np.arange(0.0,10.0,0.04)
d = np.arange(0.0,5.0,0.02)
plt.subplot2grid((3,3),(0,0),colspan=3)
plt.plot(a,np.cos(2*np.pi*a),"ro-")
#plt.show()
plt.subplot2grid((3,3),(1,0),colspan=2)
plt.plot(a,np.sin(2*np.pi*b),"b*-")
#plt.show()
plt.subplot2grid((3,3),(1,2),rowspan=2)
plt.plot(a,np.tan(2*np.pi*a),"y*-")
#plt.show()
plt.subplot2grid((3,3),(2,0),colspan=1)
plt.plot(a,np.cosh(2*np.pi*a),"g*-")
#plt.show()
plt.subplot2grid((3,3),(2,1),colspan=1)
plt.plot(a,np.sinh(2*np.pi*a),"b*-")
plt.show() 
#plt.subplot2grid((3,3),(2,2))
#plt.plot(a,np.tanh(2*np.pi*a),"y*-")
#plt.show() 