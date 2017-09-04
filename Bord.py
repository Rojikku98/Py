print("start")

def new_board():
    obj = {}
    return obj



#Fel i denhär metoden 
def count(bord,typeP,n,player):
    if typeP == "row": #x
        tot = 0
        for i in range(len(bord.keys())):
            if not(is_free(bord,n,list(bord.keys())[i][1])):
                tot = tot+1
        return tot
    elif typeP == "column":
        tot =0
        for i in range(len(bord.keys())):
            if not(is_free(bord,list(bord.keys())[i][0],n)):
                tot=tot+1
        return tot


def nearest_piece(bord,x,y):
    keys = list(bord.keys())
    temp = 0;
    best = (0,0)
    for item in keys:
        temp = (((item[0]-x)**2)+((item[1]-y)**2))**0.5
        if temp < (((keys[best[0]][0]-x)**2)+((keys[best[1]][1]-y)**2))**0.5:
             best = item
    return best
            

def place_piece(bord,x,y,player):
    if(is_free(bord,x,y)):
        bord[(x,y)] = player
        return True
    else:
        return False

def is_free(bord,x,y):
    return ((x,y) not in bord)

def move_piece(bord, x1,y1,x2,y2):
    if place_piece(bord,x2,y2,get_piece(bord,x1,y1)) :
        if remove_piece(b,x1,y1):
            return True
    return False


def remove_piece(bord, x,y):
    if not(is_free(bord,x,y)):
        del bord[(x,y)] 
        return True
    else: return False

def reset_board(bord):
    return clear(bord)

def get_piece(bord,x,y):
    if not(is_free(bord,x,y)):
        return bord[(x,y)]
    else:
        return False

    




