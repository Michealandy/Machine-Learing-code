# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 21:43:09 2018

@author: - -
"""
import numpy as np
def isEqual(cur,now):
    cur=np.mat(cur).T
    now=np.mat(now).T
    temp=abs(cur-now)
    if temp.T*temp<0.00000001:
        return True
    return False
def liner_regression(theta0,theta1,xlist,ylist):
    m = len(xlist)
    alpha = 0.05#learning rate
    temptheta0 = theta0
    temptheta1 = theta1 
    cur = [temptheta0,temptheta1]
    now = [0,0]
    times = 10000
    while times>0:  
        suma = 0
        sumb = 0
        temptheta0 = theta0
        temptheta1 = theta1 
        cur = [temptheta0,temptheta1]
        for i in range(m): 
            suma = suma + alpha*(temptheta0+temptheta1*xlist[i]-ylist[i])
            sumb = sumb + alpha*(temptheta0+temptheta1*xlist[i]-ylist[i])*xlist[i]
        theta0 = temptheta0 - suma
        theta1 = temptheta1 - sumb
        now = [theta0,theta1]
        if isEqual(cur,now):
            break
        times-=1
    return now
xlist = [1,2,4,0]
ylist = [0.5,1,2,0]
now = liner_regression(0,0,xlist,ylist)   
print(now) 
