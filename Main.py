from Board import Board
from Block import Block
from KeyBoard import KeyBoard
import time,os

board = Board(23, 13)
block = Block(board, 23, 13)
block.SetBlock(board)
keyboard = KeyBoard(block)
while True:
    os.system('cls')
    keyboard.MoveBlock()
    if not block.DownBlock(board):
        block.SetBlock(board)
    board.DrawBoard()
    time.sleep(0.5)
#block.LotateBlock(board)