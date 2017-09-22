#edvbe696


def interpret(inputExpression,info):
    
    
    postNot = removeNot(False, inputExpression)
    #print(postNot)

    if isinstance(postNot[1],str):
        
        return(returnArg(find(postNot[1],info),postNot[0]))
    elif isinstance(postNot[1][0],str) and len(postNot[1]) == 1:
        return(returnArg(find(postNot[1][0],info),postNot[0]))

    else:
        
        arg1 = removeNot(False,postNot[1][0])
        arg2 = removeNot(False,postNot[1][2])
        

        #om ett vÅ‰rde  bestÅÂr av ett argument utryck
        if isinstance(arg1[1],list):
            arg1[1] = interpret(arg1[1],info)
        if isinstance(arg2[1],list):
            arg2[1] = interpret(arg2[1],info)
        
        if checkArg(postNot[1][1]):
            if returnArg(find(arg1[1],info),arg1[0]) == returnArg(find(arg2[1],info),arg2[0]) == "true":
                return returnArg("true",postNot[0])
            else:
                return returnArg("false",postNot[0])
        elif returnArg(find(arg1[1],info),arg1[0]) == "true" or returnArg(find(arg2[1],info),arg2[0]) == "true":
                return returnArg("true",postNot[0])
        else:
            return returnArg("false",postNot[0])
        



def returnArg(svar,invert):
    if invert:
        if svar == "false":
            return "true"
        elif svar == "true":
            return "false"
    else:
        return svar


def removeNot(invert,arg):
    if len(arg) == 2 and isinstance(arg,list):
        invert = not invert
        arg = arg[1]
        return removeNot(invert,arg)

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
        #print(i,"<i  a>",a)
        if i == a:
            #print("jaaa")
            return b[i]

        
