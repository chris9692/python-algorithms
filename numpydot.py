import numpy as np
a = np.arange(81).reshape((9,9))
b = np.ones([3,3])

#pad b
np.pad(b, [(0,6),(0,6)], 'constant', constant_values=0)

#matrix production
np.dot(a, np.pad(b, [(0,6),(0,6)], 'constant', constant_values=0))

#element wise production
a * np.pad(b, [(0,6),(0,6)], 'constant', constant_values=0)
