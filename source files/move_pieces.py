import pygame as p

p.init()        # initializes pygame window
screen_width = 1400
screen_height = 800
screen = p.display.set_mode((screen_width, screen_height))
screen.fill("gray34")
p.display.set_caption("Chess Bot")
clock = p.time.Clock()

class Mouse_point(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = p.Rect(x, y, 1, 1)



def select_square(squares_dict):

    x, y = p.mouse.get_pos()
    mouse_point = Mouse_point(x, y)
    mouse_point_group = p.sprite.GroupSingle()
    mouse_point_group.add(mouse_point)
    mouse_pos = p.mouse.get_pos()
    for key, val in squares_dict.items():
        if p.sprite.groupcollide(mouse_point_group, val, False, False):
            return key
        

def select_piece(pieces_dict):
    x, y = p.mouse.get_pos()
    mouse_point = Mouse_point(x, y)
    mouse_point_group = p.sprite.GroupSingle()
    mouse_point_group.add(mouse_point)
    mouse_pos = p.mouse.get_pos()
    for key, val in pieces_dict.items():
        if p.sprite.groupcollide(mouse_point_group, val, False, False):
            return key