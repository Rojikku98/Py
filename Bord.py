class Bord:
    def __init__(self):
        self.board = [], []

    def place_piece(self,x,y,player):
        if(self.is_free(x,y)):
            self.board[x][y] = player
            return True
        else:
            return False

    def is_free(self,x,y):
        return self.board[x][y] is None

    def reset_board(self):
        self.board = [], []

    def get_piece(self,x,y):
        return self.board[x][y]

    #def nearest_piece(self):



