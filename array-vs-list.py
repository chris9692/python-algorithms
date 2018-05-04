import numpy as np

# initial an 3x3 matrix
a = np.ones((3,3))

# trying to assign an object to a(2,2) 
# ERROR
a[2,2] = [9,8,7]

# convert a to a list and assign an object to a(2,2)
a = a.tolist()
a[2][2] = [9,8,7]
