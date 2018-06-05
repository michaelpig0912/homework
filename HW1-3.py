#ref:http://www.powerxing.com/python-pick-random-element-without-repeat/
import random
import time

start = time.time()
print (random.sample(range(0,100), 5))

end = time.time()
print ("%f sec" % (end-start))