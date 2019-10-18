import sys
import random


# Hash function that accepts string key and table size
# returns position of key

def h_ascii(key, N):
    s = 0
    if key is None or len(key) == 0:
        return('Specify Key')

    else:
        for i in range(len(key)):
            s += ord(key[i])
        return s % N
    

# Gets a rolling hash function

def h_rolling(key, N):
    s = 0
    try:
        for i in range(len(key)):
            s += ord(key[i]) * p**i
        s = s % m
    except TypeError:
        print('Key must be a string')
    return s % N


# Third hash function: takes given hash index and divides it by a random number

def h_random(Key, N):
    s = 0
    try:
        for i in range(len(key)):
            s += int(ord(key[i]) / random.randint(0, 100))
    except TypeError:
        print('Key must be a string')
    return s % N
