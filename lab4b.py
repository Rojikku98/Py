#edvbe696

print("s")

def interpret(arg,info):
    
    
    rLoop = loop(False, arg)
    #print(rLoop)

    if isinstance(rLoop[1],str):
        
        return(returnArg(find(rLoop[1],info),rLoop[0]))
    elif isinstance(rLoop[1][0],str) and len(rLoop[1]) == 1:
        return(returnArg(find(rLoop[1][0],info),rLoop[0]))

    else:
        
        arg1 = loop(False,rLoop[1][0])
        arg2 = loop(False,rLoop[1][2])
        

        #om ett vÅ‰rde  bestÅÂr av ett argument
        if isinstance(arg1[1],list):
            arg1[1] = interpret(arg1[1],info)
        if isinstance(arg2[1],list):
            arg2[1] = interpret(arg2[1],info)
        
        if checkArg(rLoop[1][1]):
            if returnArg(find(arg1[1],info),arg1[0]) == returnArg(find(arg2[1],info),arg2[0]) == "true":
                return returnArg("true",rLoop[0])
            else:
                return returnArg("false",rLoop[0])
        elif returnArg(find(arg1[1],info),arg1[0]) == "true" or returnArg(find(arg2[1],info),arg2[0]) == "true":
                return returnArg("true",rLoop[0])
        else:
            return returnArg("false",rLoop[0])
        



def returnArg(svar,invert):
    if invert:
        if svar == "false":
            return "true"
        elif svar == "true":
            return "false"
    else:
        return svar


def loop(invert,arg):
    if len(arg) == 2 and isinstance(arg,list):
        invert = not invert
        arg = arg[1]
        return loop(invert,arg)

    else: 

        return [invert,arg]


def checkArg(arg):
    if  arg == "AND":
        return True
    elif arg =="OR":
        return False


def find(a,b):
    #print(b.keys())
    if a == "true":
        return "true"
    if a == "false":
        return "false"
    for i in b.keys():
        print(i,"<i  a>",a)
        if i == a:
            print("jaaa")
            return b[i]

        
