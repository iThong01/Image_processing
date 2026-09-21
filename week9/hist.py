import numpy as np
hist = np.zero(256,dtype= np.int16)
img = [[1,32,5],[84,9,4]]
for x in img.ravel():
    hist[x] += 1
# after that plot hist