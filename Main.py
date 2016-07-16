from Board import Board
from Block import Block
from KeyBoard import KeyBoard
import time,os

HEIGHT = 23
WIDTH = 12

board = Board(HEIGHT, WIDTH)
block = Block(board, board.HEIGHT, board.WIDTH)
block.SetBlock()
keyboard = KeyBoard(block)
deleteflg = True
while True:
    os.system('cls')
    deleteflg = True
    keyboard.MoveBlock()
    if not block.DownBlock():
        block.SetBlock()
    #ブロックが一列に並んでいる列を全て削除し、ブロックを削除分落下させる
    while deleteflg:
        deleteflg = block.DeleteBlock()
    board.DrawBoard()
    time.sleep(0.25)
#block.LotateBlock(board)