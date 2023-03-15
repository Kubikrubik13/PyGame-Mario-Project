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


class Sprite(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Block(pygame.sprite.Sprite):
    def __init__(self, block_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image_bl = load_image("block.jpg")
        self.image_bl = pygame.transform.scale(self.image_bl, BL_IMAGE_SIZE)
        ## (block_width, block_height) = self.image.size()
        ## Нужно сжимать изображение до такого формата
        self.block_type = block_type
        self.rect = self.image.get_rect().move(BL_IMAGE_SIZE[0] * pos_x, BL_IMAGE_SIZE[1] * pos_y)


class Student(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__(student_group)
        self.image = load_image("student.png")
        self.image_st = pygame.transform.scale(self.image_st, ST_IMAGE_SIZE)
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

## создать матрицу (прочитать txt)
def generate_level(level):
    new_player, x, y = None, None, None
    for i in range(len(level)):
        level[i] = level[i].split()
        for elem in level[i]:
            elem = str(elem)
            if elem == '.':
                elem.replace(elem, None)
            elif elem == '#':
                elem.replace(elem, 'Block')

    return level, str(Student(x, y))

def main():
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    running = True
    lvl = firstwindow_draw()
    if lvl == 1:
        generate_level(load_level('level_1.txt'))
    elif lvl == 2:
        generate_level(load_level('level_2.txt'))
    pygame.display.set_caption("Chasing the Всеросс")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] <= WIDTH / 2:
                    screen.fill((255, 255, 255))
                    lvl = 1
                elif event.pos[0] >= WIDTH / 2:
                    screen.fill((255, 255, 255))
                    lvl = 2
        pygame.display.update()


if __name__ == "__main__":
    main()