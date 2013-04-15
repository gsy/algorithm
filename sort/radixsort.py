#!usr/bin/env
# encoding: utf-8

class radixsort(object):
    def __init__(self, array, d):
        self.array = array
        self.digits = d

    def exchange(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def sort(self):
        for i in range(self.digits-1, -1, -1):
            digit_array = [str(x)[i] for x in self.array]
            print digit_array
            
            for j in range(0, len(digit_array)-1):
                for k in range(j+1, len(digit_array)):
                    if digit_array[k] < digit_array[j]:
                        tmp = digit_array[k]
                        digit_array[k] = digit_array[j]
                        digit_array[j] = tmp
                        self.exchange(j, k)
            print '-'*30
            print digit_array
            print self.array
            print

if __name__ == '__main__':
    rs = radixsort([329, 457, 657, 839, 436, 720, 355], 3)
    rs.sort()
