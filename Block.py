from Board import Board
import time,os

class Block:
    #初期化関数
    def __init__(self, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        #[[1 for i in range(self.HEIGHT)] -> col  for j in range(self.WIDTH) -> row]
        self.block = [[0 for i in range(self.WIDTH)]  for j in range(self.HEIGHT)]
    
    #ブロックセット関数
    def SetBlock(self,Board):
        self.block[5][5] = 1
        self.block[5][6] = 1
        self.block[6][5] = 1
        self.block[6][6] = 1
        #美しくない
        for y in range(board.HEIGHT):
            for x in range(board.WIDTH):
                board.board[y][x] = board.board[y][x] + self.block[y][x]

    #ブロック回転関数(未実装)
    def LotateBlock(self,Board):
        print('Test RotateBlock!!')
    
    #ブロックを1段下げる
    def DownBlock(self, Board):
        tempboard = [[0 for i in range(board.WIDTH)]  for j in range(board.HEIGHT)]
        tmpxs = []
        tmpys = []
        for y in range(board.HEIGHT - 1):
            for x in range(board.WIDTH - 1):
                    if  x > 0 and x < board.WIDTH - 1 and board.board[y][x] == 1:
                        if self.CheckSetBlock(y, x):
                            tempboard[y + 1][x] = tempboard[y + 1][x] + board.board[y][x]
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
                board.board[y][x] = 0

        for y in range(board.HEIGHT):
            for x in range(board.WIDTH):
                board.board[y][x] = board.board[y][x] + tempboard[y][x]

        return True

    #ブロック削除関数(未実装)
    def DeleteBlock(self,Board):
        flg = False
        for y in range(board.HEIGHT):
            for x in range(board.WIDTH):
                if board.block[y][x] == 1:
                    flg = True
                else:
                    flg = False
            if flg == True:
                for x in range(board.WIDTH):
                    if x > 0 and x < board.WIDTH - 1:
                        board.block[y][x] = 0
                        DownBlock()

    #ブロックがセット可能かチェックする関数
    def CheckSetBlock(self, y , x):
        if board.board[y + 1][x] == 2 and board.board[y][x] == 1:
            return False
        else:
            #print ("True")
            return True

    #ブロックを固定ブロックに変更する関数
    def HoldBlock(self, listy, listx):
        for y in listy:
            for x in listx:
                #board.DebugBoard()
                board.board[y][x] = 2
        board.DebugBoard()


board = Board(23, 13)
block = Block(23, 13)
block.SetBlock(board)
for i in range(23):
    os.system('cls')
    if not block.DownBlock(board):
        block.SetBlock(board)
    board.DrawBoard()
    time.sleep(0.5)
#block.LotateBlock(board)