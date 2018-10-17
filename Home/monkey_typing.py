#!/usr/bin/env checkio --domain=py run monkey-typing

# https://py.checkio.org/mission/monkey-typing/

# p.quote-source {        float: right;        font-size: 10px;    }
# END_DESC

def count_words(text, words):
    c = 0
    for i in words:
        if i in text.lower():
            c+=1
    return (c)
print (count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))