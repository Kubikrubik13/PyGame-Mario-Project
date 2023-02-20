import pygame
import sys
from surfacehelpfile import firstwindow_draw, load_image


class SpriteGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for sprite in self:
            sprite.get_event(event)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Block(pygame.sprite.Sprite):

    def __init__(self, block_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = load_image("block.jpg")
        (block_width, block_height) = self.image.size()
        self.rect = self.image.get_rect().move(block_width * pos_x, block_height * pos_y)


class Student(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__(student_group)
        self.image = load_image("student.png")
        self.image = self.image.convert_alpha()
        (block_width, block_height) = Block.image.size()
        self.rect = self.image.get_rect().move(block_width * pos_x + 15, block_height * pos_y + 5)
        self.pos = (pos_x, pos_y)
        self.vl = 0

    def move(self, x, y):
        self.pos = (x, y)
        (block_width, block_height) = Block.image.size()
        self.rect = self.image.get_rect().move(
            block_width * self.pos[0] + 15, block_height * self.pos[1] + 5)

    def update(self, left, right):
        if left and self.vl <= 200:
            self.vl = -20

        if right and self.vl >= -200:
            self.vl = 20

        if not (left or right):
            self.vl = 0


sprite_group = SpriteGroup()
student_group = SpriteGroup()
student = None
learning = True
clock = pygame.time.Clock()


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Block('empty', x, y)
            elif level[y][x] == '#':
                Block('wall', x, y)
            elif level[y][x] == '@':
                Block('empty', x, y)
                new_player = Student(x, y)
                level[y][x] = "."
    return new_player, x, y


def move(student, movement):
    level_map = load_level('level_1.txt')
    x, y = student.pos
    print(level_map[x][y - 1])
    print(level_map[x][y + 1])
    print(level_map[x - 1][y])
    print(level_map[x][y + 1])
    print()
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == ".":
            student.move(x, y - 1)
    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == ".":
            student.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == ".":
            student.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == ".":
            student.move(x + 1, y)


def main():
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    firstwindow_draw()
    pygame.display.set_caption("Chasing the Всеросс")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()
