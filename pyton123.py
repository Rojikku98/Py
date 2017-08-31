import numbers

print("Start")


def max3(a,b,c):
    if(a<b):
        if(b<c):
            return c
        else:
            return b
    elif(a<c):
        return c
    else: return a


def div_by_three(x):
    y = x/3
    print(x ,"divided by 3 equals",y)
    return  (x%3 == 0)


def power(x,y):
    z = x
    for i in range(y-1):
        x*=z
    return x
# --------------------------------------------------------------------------------------------


def check_pnr(arr):
    # print(10-unit(summ(produkt(arr))) ,"funktioner")# print(arr[len(arr)-1] ,"svar")
    return ((10-unit(summ(produkt(arr))))%10 == arr[len(arr)-1])
    

def summ(arr):
    tot=0
    for i in range(len(arr)):
        tot += arr[i] 
    return tot


def produkt(arr):
    arr2 = []
    #print(len(arr))
    for i in range(len(arr)-1):
        #print(i)
        x=arr[i]
        if (i%2==0):
            x=x*2
        arr2.append(unit(x))
        arr2.append(ten(x))
    return arr2


def unit(x):
    return x%10


def ten(x):
    if (x>9):
        return (x//10)%10
    else: return 0


# -------------------------------------------------------

