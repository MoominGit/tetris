from Board import Board
import time,random

class Block:
    #初期化関数
    def __init__(self, Board, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        #[[1 for i in range(self.HEIGHT)] -> col  for j in range(self.WIDTH) -> row]
        self.block = [[0 for i in range(self.WIDTH)]  for j in range(self.HEIGHT)]
        self.board = Board
    
    #ブロックセット関数
    def SetBlock(self):
    #block[2][3] = 起点
        self.block = [[0 for i in range(self.WIDTH)]  for j in range(self.HEIGHT)]
        rand_num = random.randint(1, 2)
        #print(rand_num)
        if rand_num == 1:
            self.block[0][1] = 1
            self.block[0][2] = 1
            self.block[1][1] = 1
            self.block[1][2] = 1
        elif rand_num == 2:
            self.block[0][1] = 1
            self.block[1][1] = 1
            
        #美しくない
        for y in range(self.board.HEIGHT):
            for x in range(self.board.WIDTH):
                self.board.board[y][x] = self.board.board[y][x] + self.block[y][x]

    #ブロック回転関数(未実装)
    def LotateBlock(self):
        print('Test RotateBlock!!')
    
    #ブロックを1段下げる
    def DownBlock(self):
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
                            #print("False!")
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
    def MoveLeftBlock(self):
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
    def MoveRightBlock(self):
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

    #ブロック削除関数
    def DeleteBlock(self):
        #print("delete!")
        flg = False
        tempboard = [[0 for i in range(self.board.WIDTH)]  for j in range(self.board.HEIGHT)]
        for y in reversed(range(self.board.HEIGHT - 1)):
            for x in reversed(range(self.board.WIDTH - 1)):
                #print (x, end="")
                if x > 0 and x < self.board.WIDTH - 1:
                    #固定ブロックであれば削除フラグを立てる
                    if self.board.board[y][x] == 2:
                        flg = True
                        #ブロックエリア内を橋までチェックして、削除フラグが立っていたらチェック終了
                        if(x == 1 and flg == True):
                            #print("state delete ok!")
                            break
                    else:
                        #検索途中に固定ブロック以外を発見した場合、削除せずに処理終了
                        flg = False
                        break
            if flg == True:
                break
        #print(flg)
        if flg == True:
            for x in range(self.board.WIDTH - 1):
                if x > 0 and x < self.board.WIDTH - 1:
                    #print("state delete!")
                    self.board.board[y][x] = 0

            for y in reversed(range(self.board.HEIGHT - 1)):
                for x in reversed(range(self.board.WIDTH - 1)):
                    tempboard[y + 1][x] = tempboard[y + 1][x] + self.board.board[y][x]

            #ブロックが列で埋まった場合削除
            for y in range(self.board.HEIGHT - 1):
                for x in range(self.board.WIDTH - 1):
                    if x > 0:
                        self.board.board[y][x] = 0

            #削除した後ブロックを1段落下させる
            for y in range(self.board.HEIGHT):
                for x in range(self.board.WIDTH):
                    self.board.board[y][x] = self.board.board[y][x] + tempboard[y][x]

            return True
        else:
            return False

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
                self.board.board[y][x] = 2
        #self.board.DebugBoard()