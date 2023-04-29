#!/bin/python3

import math

def progressbar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '\033[32m=\033[0m' * int(percent) + '-' * (100 - int(percent))
    if progress == total:
        print(f"\r\033[32m|\033[0m{bar}\033[32m|\033[0m Completed!", end="\n")
    else:
        
        print(f"\r\033[32m|\033[0m{bar}\033[32m|\033[0m {percent:.2f}%", end="\r")

numbers = [x*5 for x in range(2000,3000)]
results = []

progressbar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progressbar(i+1, len(numbers))

input("Press ENTER to continue.")