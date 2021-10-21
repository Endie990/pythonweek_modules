# -*- coding: utf-8 -*-
"""
Tool for measuring execution time of small code snippets.
"""

import timeit

print('Time taken to run the following code: * import random;random.sample(range(1,1000000),2).* is..')
print('...')
print()
print('..')
print()

print (timeit.timeit('import random;random.sample(range(1,1000000),2)'))



