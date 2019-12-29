import numpy as np
import time

'''Quick initialization'''

length = 4000
native_lst = []

for i in range(length):
    native_lst.append(i)

numpy_lst = np.array(native_lst)

'''Testing part starts here'''

time1 = time.perf_counter_ns()
#numpy_mean = numpy_lst.sum()/numpy_lst.size
native_mean = sum(native_lst)/len(native_lst)
print((time.perf_counter_ns()-time1))
