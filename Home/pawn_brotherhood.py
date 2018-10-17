#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

def safe_pawns(pawns):
    p = set()
    s = 0
    for i in pawns:
        row = int(i[1])-1
        col = ord(i[0])-97
        p.add((row,col))
    for row,col in p:
        if ((row - 1, col - 1)) in p or ((row - 1, col + 1) in p):
            s+=1
    return (s)
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1