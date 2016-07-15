from Board import Board
import time

class Block:
    #初期化関数
    def __init__(self, Board, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        #[[1 for i in range(self.HEIGHT)] -> col  for j in range(self.WIDTH) -> row]
        self.block = [[0 for i in range(self.WIDTH)]  for j in range(self.HEIGHT)]
        self.board = Board
    
    #ブロックセット関数
    def SetBlock(self,Board):
        self.block[5][5] = 1
        self.block[5][6] = 1
        self.block[6][5] = 1
        self.block[6][6] = 1
        #美しくない
        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                self.board.board[y][x] = self.board.board[y][x] + self.block[y][x]

    #ブロック回転関数(未実装)
    def LotateBlock(self,Board):
        print('Test RotateBlock!!')
    
    #ブロックを1段下げる
    def DownBlock(self, Board):
        tempboard = [[0 for i in range(self.board.WIDTH)]  for j in range(self.board.HEIGHT)]
        tmpxs = []
        tmpys = []
        for y in range(self.board.HEIGHT - 1):
            for x in range(self.board.WIDTH - 1):
                    if  x > 0 and x < self.board.WIDTH - 1 and self.board.board[y][x] == 1:
                        if self.CheckSetBlock(y, x, 'DOWN'):
                            tempboard[y + 1][x] = tempboard[y + 1][x] + self.board.board[y][x]
                            tmpxs.append(x)
                            tmpys.append(y)
                        else:
                            print("False!")
                            tmpxs.append(x)
                            tmpys.append(y)
                            self.HoldBlock(tmpys, tmpxs)
                            return False
        for y in tmpys:
            for x in tmpxs:
                self.board.board[y][x] = 0

        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                self.board.board[y][x] = self.board.board[y][x] + tempboard[y][x]

        return True

    #ブロックを左に移動
    def MoveLeftBlock(self, Board):
        tempboard = [[0 for i in range(self.board.WIDTH)]  for j in range(self.board.HEIGHT)]
        tmpxs = []
        tmpys = []
        for y in range(self.board.HEIGHT - 1):
            for x in range(self.board.WIDTH - 1):
                    if  x > 0 and self.board.board[y][x] == 1:
                        if self.CheckSetBlock(y, x, 'LEFT'):
                            tmpys.append(y)
                            tmpxs.append(x)
                            tempboard[y][x - 1] = tempboard[y][x - 1] + self.board.board[y][x]
                        else:
                            return False
        for y in tmpys:
            for x in tmpxs:
                self.board.board[y][x] = 0

        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                self.board.board[y][x] = self.board.board[y][x] + tempboard[y][x]

        return True

    #ブロックを右に移動
    def MoveRightBlock(self, Board):
        tempboard = [[0 for i in range(self.board.WIDTH)]  for j in range(self.board.HEIGHT)]
        tmpxs = []
        tmpys = []
        for y in range(self.board.HEIGHT - 1):
            for x in range(self.board.WIDTH - 1):
                    if  x > 0 and self.board.board[y][x] == 1:
                        if self.CheckSetBlock(y, x, 'RIGHT'):
                            tmpys.append(y)
                            tmpxs.append(x)
                            tempboard[y][x + 1] = tempboard[y][x + 1] + self.board.board[y][x]
                        else:
                            return False
        for y in tmpys:
            for x in tmpxs:
                self.board.board[y][x] = 0

        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                self.board.board[y][x] = self.board.board[y][x] + tempboard[y][x]

        return True

    #ブロック削除関数(未実装)
    def DeleteBlock(self,Board):
        flg = False
        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                if self.board.block[y][x] == 1:
                    flg = True
                else:
                    flg = False
            if flg == True:
                for x in range(self.board.WIDTH):
                    if x > 0 and x < self.board.WIDTH - 1:
                        self.board.block[y][x] = 0
                        DownBlock()

    #ブロックがセット可能かチェックする関数
    def CheckSetBlock(self, y , x, vector):
        if vector == 'LEFT':
            if self.board.board[y][x - 1] == 2 and self.board.board[y][x] == 1:
                return False
            else:
                return True
        elif vector == 'RIGHT':
            if self.board.board[y][x + 1] == 2 and self.board.board[y][x] == 1:
                return False
            else:
                return True
        else:
            if self.board.board[y + 1][x] == 2 and self.board.board[y][x] == 1:
                return False
            else:
                return True

    #ブロックを固定ブロックに変更する関数
    def HoldBlock(self, listy, listx):
        for y in listy:
            for x in listx:
                #board.DebugBoard()
                self.board.board[y][x] = 2
        self.board.DebugBoard()