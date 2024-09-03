import random

from algorithms import *


l = list(range(15))
random.shuffle(l)


print(l)
quick_sort(l)
print(l)