from pyautogui import click
from math import floor

from config import DIFFICULTY


def clickCell(location: tuple, button="LEFT"):
    x, y = location

    BOARD_POS_P0 = DIFFICULTY[1][0]
    CELL_SIZE = 50
    CELL_OFFSET_X, CELL_OFFSET_Y = 25, 25

    click(
        x=(BOARD_POS_P0[0] + CELL_OFFSET_X + x * CELL_SIZE),
        y=(BOARD_POS_P0[1] + CELL_OFFSET_Y + y * CELL_SIZE),
        button=button,
    )


def initialClick():
    return clickCell((floor(DIFFICULTY[0][0] / 2), floor(DIFFICULTY[0][1] / 2)))

def rclickCell(location: tuple):
    clickCell(location, button="RIGHT")

def mclickCell(location: tuple):
    clickCell(location, button="MIDDLE")