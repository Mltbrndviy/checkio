#!/usr/bin/env checkio --domain=py run cipher-map2

# https://py.checkio.org/mission/cipher-map2/

# 
# END_DESC

import numpy as np
def recall_password(cipher_grille, ciphered_password):
    def lopata(passw,text):
        clean_key = np.array([list(x) for x in list(passw)])
        clean_text = np.array([list(x) for x in list(text)])
        return clean_key,clean_text
    answ = []
    def rotate(clean_key):
        return [x[::-1] for x in zip(*clean_key)]
    clean_key,clean_text = lopata(cipher_grille, ciphered_password)
    for j in range(4):
        for i in range(4):
            answ+=[x[1] for x in zip(clean_key[i],clean_text[i]) if x[0]!="."]
        clean_key = rotate(clean_key)
    return ("".join(answ))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'