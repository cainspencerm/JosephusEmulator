import numpy as np
from curtsies.fmtfuncs import red, green
import sys
import argparse


def countDead(circle):
    i = 0
    for a in circle:
        if a == 0:
            i += 1
    return i


def printCircle(n, pos, circle, dead):    
    print('[ ', end='')
    for a, b, i in zip(dead, circle, np.arange(n)):
        if a == 0:
            print(red(str(b)), end='')
        elif i == pos:
            print(green(str(b)), end='')
        else:
            print(b, end='')

        print(' ', end='')

    print(']')


# Determine position for Josephus to survive.
def printSafePosition(n=41, survivors=1, verbose=False):
    circle = np.arange(n+1)[1:]
    dead = np.arange(n+1)[1:]

    k = 0
    pos = 0
 
    if verbose:
        print('--------------- N = ' + str(n) + ' ----------------')
        printCircle(n, pos, circle, dead)

    while n - countDead(dead) > survivors:       
        # Skip survivor
        k = (k + 1) % n

        while dead[k] == 0:
            k = (k + 1) % n
    
        dead[k] = 0

        while dead[k] == 0:
            k = (k + 1) % n

        pos = k

        # Print current setup
        if verbose:
            printCircle(n, pos, circle, dead)

    if not verbose:
        printCircle(n, pos, circle, dead)


parser = argparse.ArgumentParser(description='Determine the Josephus survivors')
parser.add_argument('count', type=int)
parser.add_argument('-s', '--survivors', type=int, default=1)
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-a', '--all', action='store_true')

args = parser.parse_args()

if args.all:
    for i in range(args.survivors, args.count):
        printSafePosition(i, args.survivors, args.verbose)
    
printSafePosition(args.count, args.survivors, args.verbose)
