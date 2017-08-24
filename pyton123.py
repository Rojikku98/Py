print("Start")


def max3(a,b,c):
    if(a<b):
        if(b<c):
            return c
        else:
            return b
    elif(a<c):
        return c
    else : return a
