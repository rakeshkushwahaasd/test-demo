import numpy as np
b=np.array([21,22,33,12,2,4,8,6])
a=np.array([1,3,56,43,43,34,45,23])
c=a[b%2 == 0]
a[b%2 == 0]=-1
c[2]=10
print(a)
print(c)