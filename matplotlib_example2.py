# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:06:29 2017
实现直方图的绘制
@author: mav
"""

# -*- coding: utf-8 -*-




import matplotlib.pyplot  as plt
import matplotlib.gridspec as gridespec
gs = gridespec.GridSpec(3,3)#规定一个确定的区域。
#import matplotlib as mt
import numpy as np
N=20#极坐标图的图形个数
thera = np.linspace(0.0,2*np.pi,N,endpoint=False)
#用linspase等分出N个角度
radii = 10*np.random.rand(N)#每个角度对应的值
width = np.pi /4* np.random.rand(N)#给出每个值所对应宽度之

ax =plt.subplot(111,projection='polar')#111一个区域，极坐标图
bars = ax.bar(thera,radii,width=width,bottom=0.0)
for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
#np.random.seed(0)
#a = np.random.normal(mu,sigma,size=100)
#print(a)
#labels = "froges",'dogs','hogs',"logs"
#sizes  =[10,30,45,15]
#expor  =[0.2,0,0.1,0]
#plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
#plt.pie(sizes,expor,labels=labels,autopct="%1.1f%%",shadow=True,startangle=90)
#   autopcts 表示中间显示百分数的方式。
#plt.hist(a,40,normed=1,histtype='stepfilled',facecolor='g',alpha=0.95)
#plt.axis("equal")
plt.title('test')
plt.show() 
