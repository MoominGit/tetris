# _*_ coding: shift-jis _*_
class Board:
    #HEIGHT = 23
    #WIDTH = 13
    #初期化関数
    def __init__(self, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        self.board = [[0 for i in range(self.WIDTH)]  for j in range(self.HEIGHT)]
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if x == 0:
                    self.board[y][x] = 2
                if x == self.WIDTH - 1:
                    self.board[y][x] = 2
                if y == self.HEIGHT - 1:
                    self.board[y][x] = 2
        print("init!")

    #ボード描画関数
    def DrawBoard(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.board[y][x] == 0:
                    print('  ', end="")
                else:
                    print('□', end="")
            print()

    #デバッグ用変数描画関数
    def DebugBoard(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                print(str(self.board[y][x] )+ ' ', end="")
            print()
