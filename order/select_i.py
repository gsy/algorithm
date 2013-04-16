#!/usr/bin/env python
# encoding: utf-8
import random

class selection(object):
    def __init__(self, array):
        self.array = array

    def exchange(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def partition(self, p, r):
        x = self.array[r]
        i = 0
        k = p-1

        print '-'*10 + ' origin array ' + '-'*10
        print self.array

        for j in range(p, r):
            if self.array[j] < x:
                k = k + 1
                i = i + 1
                self.exchange(k, j)
                
        self.exchange(k+1, r)
        print '-'*10 + ' exchanged:%d ' % (i+1,) + '-'*10
        print self.array
        return i+1

    def random_partition(self, p, r):
        i = random.randint(p, r)
        self.exchange(i, r)
        return self.partition(p, r)

    def select(self, p, r, i):
        if p == r:
            return self.array[p]

        k = self.random_partition(p, r)
        if k == i:
            return self.array[k]
        elif k > i:
            return self.select(p, k-1, i)
        else:
            return self.select(k+1, r, i-k)            

if __name__ == '__main__':
    ls = [3, 5, 6, 1, 2, 10]
    s = selection(ls)
    print s.select(0, len(ls)-1, 3)
