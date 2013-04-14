#!/usr/bin/env python
# encoding: utf-8
class heap(object):
    """heap"""
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)

    def get_parent(self, i):
        if i == 0:
            return -1
        
        if (i%2 == 1):
            return self.array[i/2]
        else:
            return self.array[i/2-1]
        
    def get_left_child(self, i):
        if (2*i+1) >= self.size:
            return None
        else:        
            return self.array[2*i+1]

    def get_right_child(self, i):
        if (2*i+2) >= self.size:
            return None
        else:
            return self.array[2*i+2]

    def exchange(self, i, j):
        """exchange item i and item j"""
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def show(self):
        tmp = [str(item) for item in self.array]
        print ' '.join(tmp)    

class max_heap(heap):
    def __init__(self, array):
        super(max_heap, self).__init__(array)
        
    def max_heapify(self, i):
        if i == -1:
            return
        
        max = self.array[i]
        left = self.get_left_child(i)
        right = self.get_right_child(i)

        max_index = i        
        if (left != None and left > max):
            max = left
            max_index = 2*i+1
        if (right != None and right > max):
            max = right
            max_index = 2*i+2

        if (i != max_index):            
            self.exchange(i, max_index)
            self.show()
            if i%2 == 1:
                self.max_heapify(i/2)
            else:
                self.max_heapify(i/2-1)

    def build_max_heap(self):
        for i in range(0, self.size/2):
            # print i
            self.max_heapify(i)

    def heap_sort(self):
        result = []
        for i in range(0, len(self.array)/2):
            self.build_max_heap()
            tmp = self.array.pop(0)
            result.append(tmp)

        return result

    def another_heap_sort(self):
        for i in range(0, self.size):
            self.build_max_heap()
            self.exchange(0, (self.size - 1))
            self.size = self.size - 1
            print '-'*25
            self.show()
            print 
                        
        
if __name__ == '__main__':
    h = max_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    # h.build_max_heap()
    # result = h.heap_sort()
    # print result
    h.another_heap_sort()
