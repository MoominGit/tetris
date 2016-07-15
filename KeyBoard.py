from Block import Block
from Board import Board
import ctypes

class KeyBoard:
    #初期化関数
    def __init__(self, Block):
        self.WIDTH = 80
        self.LEFT = 0x25
        self.RIGHT = 0x27
        self.DOWN = 0x28
        self.block = Block
        self.board = Board

    def getkey(self,key):
        return(bool(ctypes.windll.user32.GetAsyncKeyState(key)&0x8000))

    def MoveBlock(self):
        if self.getkey(self.LEFT):
            self.block.MoveLeftBlock(self.board)
        if self.getkey(self.RIGHT):
            self.block.MoveRightBlock(self.board)
           