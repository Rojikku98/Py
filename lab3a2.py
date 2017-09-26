#edvbe696
"""
-------------------------------------------------
Överlag bra skrivna funktioner! Titta på kommentarerna för "count" och "nearest_piece" 
och se om du kan skriva om dessa lite.

Ett generellt tips är att vi inte behöver else: satsen i de flesta funktionerna.
Utan vi kan retunera direkt, eftersom det finns en "osynlig" else ändå.
-------------------------------------------------
"""


"""
-------------------------------------------------
Behöver vi deklarera en variabel innan 
vi returnerar det tomma brädet?
-------------------------------------------------
"""
def new_board():
    obj = {}
    return obj


"""
-------------------------------------------------
Här bär vi endast ha en deklarerad for-loop för att korta ned koden.

Ett annat tips är att i Python finns for-loopar på detta sätt:

for key in board:
    ...

Där key i vårt fall kommer vara en tupel (x, y). Användningen av den for-loopen skulle
kunna hjälpa till att göra den här koden mycket mer läsbar.
-------------------------------------------------
"""
def count(bord,typeP,n,player):
    if typeP == "column": #x
        tot = 0
        for i in range(len(bord.keys())):
            if (n == list(bord.keys())[i][0]):
                if (get_piece(bord,n,list(bord.keys())[i][1])==player):
                    tot = tot+1
        return tot
    elif typeP == "row":
        tot =0
        for i in range(len(bord.keys())):
            if (n == list(bord.keys())[i][1]):
                if (get_piece(bord,list(bord.keys())[i][0],n)==player):
                    tot = tot+1
        return tot


"""
-------------------------------------------------
Värt att tänka på: Varför kopierar vi och gör en ny lista med keys?
Och sedan loopar igenom den istället för Brädet i sig? När man loopar igenom
en dict så loopar man genom nycklarna i dictionarien.

Funktionen bör inte kopiera nycklarna, och istället för två st
variabler för bestX/Y, kan vi inte bara ha en som är en tupel av dessa?
-------------------------------------------------
"""
def nearest_piece(bord,x,y):
    keys = list(bord.keys())
    if(len(keys)<1):
       return False
    temp = 0
    bestX = keys[0][0]
    bestY = keys[0][1]
    for item in keys:
        temp = (((item[0]-x)**2)+((item[1]-y)**2))**0.5
        if temp < (((bestX-x)**2)+((bestY-y)**2))**0.5:
             bestX = item[0]
             bestY = item[1]
    return (bestX,bestY)
            

"""
-------------------------------------------------
Snyggt! Bra, lättläst och kort.
-------------------------------------------------
"""
def place_piece(bord,x,y,player):
    if(is_free(bord,x,y)):
        bord[(x,y)] = player
        return True
    else:
        return False

def is_free(bord,x,y):
    return ((x,y) not in bord)

def move_piece(bord, x1,y1,x2,y2):
    if is_free(bord,x2,y2) and not is_free(bord,x1,y1):
        if place_piece(bord,x2,y2,get_piece(bord,x1,y1)) :
            if remove_piece(bord,x1,y1):
                return True
    return False


"""
-------------------------------------------------
Snyggt!
-------------------------------------------------
"""
def remove_piece(bord, x,y):
    if not(is_free(bord,x,y)):
        del bord[(x,y)] 
        return True
    else: return False

def reset_board(bord):
    return bord.clear()

def get_piece(bord,x,y):
    if not(is_free(bord,x,y)):
        return (bord[(x,y)])
    else:
        return False

    




