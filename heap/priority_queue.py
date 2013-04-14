#!/usr/bin/env python
# encoding: utf-8
from max_heap import max_heap

class priority_queue(max_heap):
    def __init__(self, array):
        super(max_heap, self).__init__(array)
    
    def insert(self, x):
        """insert x into queue"""
        self.array.append(x)
        self.size = len(self.array)
        self.build_max_heap()

    def maximum(self):
        """get maximum item from queue"""
        self.build_max_heap()
        return self.array[0]

    def extract_max(self):
        """get maximum item from queue and then remove it"""
        self.build_max_heap()
        return self.array.pop(0)

    def increase_key(self, i, key):
        """increase element i's key to k where k >= i's original key"""
        if self.array[i] > key:
            raise ValueError, "insert key must not less than original key"
        self.array[i] = key
        while(i != 0):
            p = self.get_parent(i)
            if (self.array[i] > p):
                if (i%2 == 1):
                    self.exchange(i, i/2)
                else:
                    self.exchange(i, i/2-1)                
            i = i/2        

if __name__ == '__main__':
    pq = priority_queue([14, 16, 10, 8, 7, 9, 3, 2, 4, 1])
    # print pq.extract_max()
    # pq.show()
    # pq.increase_key(3, 11)
    # pq.show()
    print pq.maximum()
