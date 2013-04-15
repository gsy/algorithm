#!/usr/bin/env python
# encoding: utf-8

class countsort(object):
    """
    Sort an array whose element range in 0 to k 
    """
    def __init__(self, array, k):
        self.array = array
        self.range = k
        self.count_array = []
        self.result_array = []
        for i in range(0, self.range):
            self.count_array.append(0)

        for i in range(0, len(self.array)):
            self.result_array.append(0)
        
    def sort(self):
        # make count array
        for i in self.array:
            self.count_array[i] = self.count_array[i] + 1
        for j in range(0, len(self.count_array)-1):
            self.count_array[j+1] = self.count_array[j+1] + self.count_array[j]
        print self.count_array
            
        for x in self.array:            
            self.result_array[self.count_array[x]-1] = x
            self.count_array[x] = self.count_array[x] - 1
            print self.result_array
            
        return self.result_array            

if __name__ == '__main__':
    ls = [2, 5, 3, 0, 2, 3, 0, 3]
    cs = countsort(ls, 6)
    cs.sort()


            
            
        
        
        
