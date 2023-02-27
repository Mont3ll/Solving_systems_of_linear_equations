import numpy as np
from scipy import linalg

a=np.array([[9,3,1],[4,-2,1],[1,1,1]])
b=np.array([25,20,5])
x=linalg.solve(a,b)
print(x)
