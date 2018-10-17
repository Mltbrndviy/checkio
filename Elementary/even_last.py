#!/usr/bin/env checkio --domain=py run even-last

# https://py.checkio.org/mission/even-last/

# You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)    then    multiply this summed number and the final element of the array together. Don't forget that the first element has an    index of 0.
# 
# For an empty array, the result will always be 0 (zero).
# 
# Input:A list of integers.
# 
# Output:The number as an integer.
# 
# Precondition:0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
# 
# 
# 
# END_DESC

def checkio(array):
    if array:
        s = 0
        for i in range(len(array)):
            if i%2 == 0:
                s+=array[i]
        return s*array[i]
    else:
        return 0
print (checkio([5,8,4]))