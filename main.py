import pygame
import sys
import os
from surfacehelpfile import firstwindow_draw, load_image

size = width, height = 300, 300
block_width, block_height = 20, 20


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


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
        ## Нужно сжимать изображение до такого формата
        self.block_type = block_type
        self.rect = self.image.get_rect().move(block_width * pos_x, block_height * pos_y)


class Student(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__(student_group)
        self.image = load_image("student.png")
        self.image = self.image.convert_alpha()  ## Лучше запихнуть внутрь load_image
        # (block_width, block_height) = Block.image.size()  ## Нельзя так писать!
        self.x, self.y = block_width * pos_x + 15, block_height * pos_y + 5
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.pos = (pos_x, pos_y)
        self.vl = 0

    def move(self, vl_x, vl_y=0):
        self.x += vl_x
        self.y += vl_y
        self.rect = self.image.get_rect().move(self.x, self.y)
        ## Весь метод неверный
        '''self.pos = (x, y)
        #(block_width, block_height) = Block.image.size() 
        self.rect = self.image.get_rect().move(
            block_width * self.pos[0] + 15, block_height * self.pos[1] + 5)'''

    def update(self, left, right):
        if left and self.vl <= 200:
            self.vl = -20

        if right and self.vl >= -200:
            self.vl = 20

        if not (left or right):
            self.vl = 0
        self.move(vl)


sprite_group = SpriteGroup()
student_group = SpriteGroup()
student = None
learning = True
clock = pygame.time.Clock()


def load_level(filename):
    filename = os.path.join("data", filename)
    with open(filename, 'r') as map_file:
        level_map = [line.strip() for line in map_file]
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
    generate_level(level_map)
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
        if y < height - 1 and level_map[y + 1][x] == ".":
            student.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == ".":
            student.move(x - 1, y)
    elif movement == "right":
        if x < width - 1 and level_map[y][x + 1] == ".":
            student.move(x + 1, y)


def main():
    pygame.init()
    size = width, height
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
