import pygame
import sys
import os
from const import WIDTH, HEIGHT, BL_IMAGE_SIZE, ST_IMAGE_SIZE
from surfacehelpfile import firstwindow_draw, load_image


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class SpriteGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for sprite in self:
            sprite.get_event(event)


sprite_group = SpriteGroup()
student_group = SpriteGroup()
student = None
learning = True
clock = pygame.time.Clock()


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
        self.image = pygame.transform.scale(self.image, BL_IMAGE_SIZE)
        ## (block_width, block_height) = self.image.size()
        ## Нужно сжимать изображение до такого формата
        self.block_type = block_type
        self.rect = self.image.get_rect().move(BL_IMAGE_SIZE[0] * pos_x, BL_IMAGE_SIZE[1] * pos_y)

    def __str__(self):
        return f'Block {self.block_type} at {self.rect}'

    def __repr__(self):
        return f'Block {self.block_type} at {self.rect}'


class Student(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(student_group)
        self.image = load_image("student.png")
        self.image = pygame.transform.scale(self.image, ST_IMAGE_SIZE)
        self.x, self.y = BL_IMAGE_SIZE[0] * pos_x + 15, BL_IMAGE_SIZE[1] * pos_y + 5
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

    def update(self, left, right, up, down):
        if left and self.vl <= 200:
            self.vl -= 20

        if right and self.vl >= -200:
            self.vl += 20

        if not (left or right):
            self.vl += 0
        self.move(self.vl)

    def __str__(self):
        return f'Student at {self.x, self.y}'

    def __repr__(self):
        return f'Student at {self.x, self.y}'


def load_level(filename):
    filename = os.path.join("data", filename)
    with open(filename, 'r') as map_file:
        level_map = [line.strip() for line in map_file]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


## создать матрицу (прочитать txt)
def generate_level(level):
    new_player = None
    game_field = []
    for i in range(len(level)):
        line = []
        for j, elem in enumerate(level[i]):
            if elem == '.':
                line.append(None)
            elif elem == '#':
                line.append(Block('Block', j, i))
            elif elem == '@':
                line.append(None)
                new_player = Student(j, i)
        game_field.append(line[:])

    return game_field, new_player


def fill_sprite_group(sprite_group, array, filtering):
    pass


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    firstwindow_draw()
    lvl_number = 1
    lvl = None
    if lvl_number == 1:
        lvl = generate_level(load_level('level_1.txt'))
    elif lvl_number == 2:
        lvl = generate_level(load_level('level_2.txt'))
    print(sprite_group)
    for i in sprite_group:
        print(i)
    pygame.display.set_caption("Chasing the Всеросс")
    game_condition = 'starting_screen'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif game_condition == 'starting_screen':
                if event.type == pygame.MOUSEBUTTONUP:
                    game_condition = 'started_level'
                    if event.pos[0] <= WIDTH / 2:
                        screen.fill((255, 255, 255))
                        lvl = 1
                    elif event.pos[0] >= WIDTH / 2:
                        screen.fill((255, 255, 255))
                        lvl = 2
            elif game_condition == 'started_level':
                sprite_group.draw(screen)
                student_group.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()