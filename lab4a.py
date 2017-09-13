#edvbe696

print("start")

lowercase = "qwertyuiopåasdfghjklöäzxcvbnm_."
uppercase = "QWERTYUIOPÅASDFGHJKLÖÄZXCVBNM |"

def split_rec(string):
    totC = ""
    totL = ""

    return loop(string,totC,totL)


def loop(string,totC,totL):
    if string[0] in lowercase:
        totL += string[0]
    elif string[0] in uppercase:
        totC += string[0]
    string = string[1:]
    if len(string)==0:
        return (totL,totC)
    else:
        return loop(string,totC,totL)


def split_it(string):
    totL = ""
    totC = ""
    for i in range(len(string)):
        if string[i] in lowercase:
            totL = totL + string[i] 
        elif string[i] in uppercase:
            totC = totC + string[i]
    return (totL,totC)
    
