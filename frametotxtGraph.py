# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:38:06 2021

@author: moeez
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2


imageNo = 10

for i in range(imageNo):
    image = 'photos/image_'+ str(i+1) +'.jpg'
    img = cv2.imread(image)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection='3d')
    for x, c, z in zip([h,s,v], ['r', 'g', 'b'], [30, 20, 10]):
        xs = np.arange(256)
        ys = cv2.calcHist([x], [0], None, [256], [0,256])
        cs = [c] * len(xs)
        cs[0] = 'c'
        ax.bar(xs, ys.ravel(), zs=z, zdir='y', color=cs, alpha=0.8)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    f=open("histogram.txt","a+")
    histo = repr(h)
    f.write(histo)
    histo = repr(s)
    f.write(histo)
    histo = repr(v)
    f.write(histo)
    f.writelines("\n")
    f.writelines("\n")
    f.writelines("\n")
    f.close()


