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
        self.rect = p.Rect(x, y, x, y)

x, y = p.mouse.get_pos()
mouse_point = Mouse_point(x, y)
mouse_point_group = p.sprite.GroupSingle()
mouse_point_group.add(mouse_point)


def select_square(squares_dict):

    x, y = p.mouse.get_pos()
    mouse_point = Mouse_point(x, y)
    mouse_point_group = p.sprite.GroupSingle()
    mouse_point_group.add(mouse_point)
    mouse_pos = p.mouse.get_pos()
    for event in p.event.get():
        if event.type == p.MOUSEBUTTONDOWN:
            for key, val in squares_dict.items():
                if p.sprite.groupcollide(mouse_point_group, val, False, False):
                    print(mouse_pos)
                else:
                    print("Not clicking a square")