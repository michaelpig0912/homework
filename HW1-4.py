#ref:http://imsardine.simplbug.com/note/random/python.html
import random
import numpy as np
import time

a = input("input:")
try:
	b = int(a)
except:
	Pass()
start = time.time()
c = [random.uniform(-1, 1) for i in range(b) ] 
print (c)
d = np.mean(c)
print (d)
e = np.std(c)
print (e)

end = time.time()
print ("%f sec" % (end-start))