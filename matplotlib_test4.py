#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:41:19 2017

@author: xwz
"""

import matplotlib.pyplot  as plt
import numpy as np
a=np.arange(10)
plt.plot(a,a*1.5,"go-",a,a*2.5,"r-x",a,a*3.5,"m-.v",a,a*4.5,"c:d")
plt.show()
