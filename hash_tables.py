import hash_functions
import sys
import time
import random

class LinearProbe:

    def __init__(self, N, hash_function):
        """
        returns object, size, and keys from hash table

        N: length of the hash array
        T: array to hold the (key, value) tuples
        M: number of indexes occupied by (key, value)
        """
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        """adds keys and values"""

        start_hash = self.hash(key, self.N)
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        else:
            return False

    def search(self, key):
        """Searches for key in hash table """

        hash_slot = self.hash(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        else:
            return None

class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        self.T[start_hash] = self.hash(key, self.N)
        self.M += 1
        return True

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for k, v in self.T[start_hash]:
            if key == k:
                return v
        return None

if __name__ == '__main__':

    N = int(sys.argv[1])
    hash_alg = sys.argv[2]
    collision_strategy = sys.argv[3]
    data_file_namem = sys.argv[4]
    keys_to_add = int(sys.argv[5])

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_ascii_sum)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_ascii_sum)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_polynomial_rolling)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_polynomial_rolling)

    elif hash_alg == 'python':
        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_python)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_python)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.insert(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            sys.exit
