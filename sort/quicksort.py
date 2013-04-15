#!/urs/bin/env
# encoding: utf-8

class quicksort(object):
    def __init__(self, array):
        self.array = array

    def sort(self, p, r):
        """
        quick sort
        
        @param p: left side of unsorted array
        @param r: right side of unsorted array
        """
        if p >= r:
            return
        
        q = self.partition(p, r)
        self.sort(p, q-1)
        self.sort(q+1, r)

    def exchange(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def show(self):
        print ' '.join([str(x) for x in self.array])

    def partition(self, p, r):
        """
        devide the unsorted array into two parts, return the partition value
        """
        x = self.array[r]
        i = p-1
        for j in range(p, r):
            if self.array[j] <= x:
                i = i+1
                if (i != j):
                    # print "exchange %d and %d" % (i, j)                
                    self.exchange(i, j)
                
        self.exchange(r, i+1)
            
        # print '-'*20
        # self.show()
        
        return i+1

if __name__ == '__main__':
    ls = [2, 8, 7, 1, 3, 5, 6, 4]
    qs = quicksort(ls)
    qs.show()
    qs.sort(0, len(ls)-1)
    qs.show()
    
    # ls = [2, 1, 3]
    # qs = quicksort(ls)
    # qs.partition(0, len(ls)-1)
