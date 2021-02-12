'''
plotter_example.py
use with plotter button in mu editor to see how it can use tuple data and
generate a live plot of the data
'''


import time
import random

while True:
    # Just keep emitting three random numbers in a Python tuple.
    time.sleep(0.05)
    print((random.randint(0, 100), random.randint(-100, 0), random.randint(-50, 50)))
