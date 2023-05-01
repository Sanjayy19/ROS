import numpy as np
import math

#link parameters
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

#joint variables
d1 = float(input("x1 = "))
T2 = float(input("T2 = "))
T3 = float(input("T3 = "))

#degree to radian
T2=(T2/180.0)*np.pi
T3=(T3/180.0)*np.pi

#table (theta,alpha,r,d)
PT = [[(0.0/180.0*np.pi),(0.0/180.0*np.pi),0,a1+d1],[[T2,(0.0/180.0*np.pi),a2,0]],[[T3,(0.0/180.0*np.pi),a4,a3]]]

#Homo Trans Matrix
i=0
H0_1 = [[np.cos(PT[0][0]),-np.sin(PT[0][0]*np.cos(PT[0][1]))],[],[],[]]