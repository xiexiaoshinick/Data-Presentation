#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:19:57 2017

@author: xwz
"""
import matplotlib.pyplot as plt
plt.plot([3,1,4,5,2])
plt.ylabel('Grade')
plt.xlabel('Person')
plt.savefig('/home/xwz/文档/test',dpi=600)
plt.show()