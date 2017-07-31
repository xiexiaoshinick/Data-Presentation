#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:25:44 2017

@author: xwz
"""
import matplotlib.pyplot as plt
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('Grade')
plt.xlabel('Person')
plt.axis([0,10,0,10])#设定x和y的使用范围
plt.savefig('/home/xwz/文档/test',dpi=600)
plt.show()
