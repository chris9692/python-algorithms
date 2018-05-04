import numpy as np
a = np.arange(81).reshape((9,9))

#pick 3 values
a[[0,1,2], [0,1,2]]

#pick 9 values
a[np.ix_([0,1,2], [0,1,2])]
