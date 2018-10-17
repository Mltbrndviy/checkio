#!/usr/bin/env checkio --domain=py run house-password

# https://py.checkio.org/mission/house-password/

# 
# END_DESC

def checkio(data):
    if len(data)>= 10:
        for i in range(len(data)):
            if data[i].isdigit() == True:
                if data.islower() == False and data.isupper() == False and data.isdigit()==False:
                    return True
    else:
        return False
print (checkio('QwErTy911poqqqq'))