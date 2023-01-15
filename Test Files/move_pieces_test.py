import pygame as p

def select_square(board_group):
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            x, y = p.mouse.get_pos()
            board_group.square