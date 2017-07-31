#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:40:08 2017

@author: xwz
"""

import matplotlib.pyplot as plt
import numpy as np
def f(t) :
    return np.exp(-t) *np.cos(2*np.pi*t)

a=np.arange(0.0,5.0,0.02)
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),"r--")

plt.savefig('/home/xwz/文档/test3',dpi=600)
plt.show()