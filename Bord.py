print("start")

def new_board():
    obj = {{},{}}
    return obj



def place_piece(bord,x,y,player):
    if(is_free(bord,x,y)):
        bord[x][y] = player
        return True
    else:
        return False

def is_free(bord,x,y):
    return bord[x],[y] is None

def reset_board(bord):
    bord = [], []

def get_piece(bord,x,y):
    return bord[x][y]

#def nearest_piece(self):




