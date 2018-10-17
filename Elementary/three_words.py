#!/usr/bin/env checkio --domain=py run three-words

# https://py.checkio.org/mission/three-words/

# Let's teach the Robots to distinguish words and numbers.
# 
# You are given a string with words and numbers separated by whitespaces (one space).    The words contains only letters.    You should check if the string contains three words insuccession.    For example, the string "start 5one two three7 end" contains three words in succession.
# 
# Input:A string with words.
# 
# Output:The answer as a boolean.
# 
# Precondition:The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
# 
# 
# END_DESC

def checkio(words):
    count = 0
    for i in words.split():
        if i.isalpha() == True:
            count+=1
            if count>=3:
                return True
        else:
            count = 0
    return False
print (checkio('JJF JKHF are over 9000'))