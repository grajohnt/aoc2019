import numpy as np
from scipy.misc import toimage

im = []

w = 25 
h = 6 

with open('d8.txt') as f:
 for line in f:
  ln = line.strip()
  for c in str(ln):
   im.append(int(c))

l = len(im)/w/h 
l = int(l)

image = np.reshape(im,(l,h,w))
# Ugh - that's layer, row, column - I hate numpy

result = np.empty([h,w]) 

for j in range(h):
 for k in range(w):
  pixind = np.nonzero(image[:,j,k]-2)
  val = image[pixind[0][0],j,k]-2
  if val == -2:
   result[j,k] = 0
  elif val == -1:
   result[j,k] = 1

print(result)
toimage(result).show()


