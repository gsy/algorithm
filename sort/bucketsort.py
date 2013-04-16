#!/usr/bin/env python
# encoding: utf-8
import math
class bucketsort(object):
    def __init__(self, array):
        self.array = array
        self.bucket = []

    def sort(self):
        for i in range(10):
            self.bucket.append([])
            
        for x in self.array:
            id = int(math.floor(10*x))
            print '%d: %g' % (id, x)
            self.bucket[id].append(x)
            self.bucket[id].sort()

        result = []
        for ls in self.bucket:
            if ls:
                for x in ls:
                    result.append(x)
                    
        print result            

if __name__ == '__main__':
    ls = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    bs = bucketsort(ls)
    bs.sort()
