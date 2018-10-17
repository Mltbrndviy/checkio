#!/usr/bin/env checkio --domain=py run non-unique-elements

# https://py.checkio.org/mission/non-unique-elements/

# If you have 50 different plug types, appliances wouldn't be available and would be very        expensive. But once an electric outlet becomes standardized, many companies can design        appliances, and competition ensues, creating variety and better prices for consumers.
# -- Bill Gates
# 
# You are given a non-empty list of integers (X).    For this task, you should return a list consisting of only the non-unique elements in this list.    To do so you will need to remove all unique elements (elements which are contained in a given    list only once).    When solving this task, do not change the order of the list.    Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# 
# 
# 
# Input:A list of integers.
# 
# Output:The list of integers.
# 
# 
# How it is used:This mission will help you to understand how to manipulate arrays,    something that is the basis for solving more complex tasks.    The concept can be easily generalized for real world tasks.    For example: if you need to clarify statistics by removing low frequency elements (noise).
# 
# You can find out more about Python arrays inone of our articles featuring lists, tuples, array.array and numpy.array.
# 
# Precondition:
# 0 < len(data) < 1000
# 
# 
# 
# END_DESC

#Your optional code here
#You can import some modules or create additional functions


def checkio(data):
    a = []
    for i in data:
        if data.count(i)>1:
            a.append(i)
    return a
print (checkio([1, 2, 3, 1, 3]))

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list