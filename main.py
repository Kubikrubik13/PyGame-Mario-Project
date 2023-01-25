import pygame
from surfacehelpfile import firstwindow_draw


class Block(pygame.sprite.Sprite):

    image = load_image("block.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Student.image
        self.rect = self.image.get_rect()


class Student(pygame.sprite.Sprite):

    image = load_image("student.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Student.image
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, left, right):
        if left and self.vl <= 200:
            self.vl = -20

        if right and self.vl >= -200:
            self.vl = 20

        if not (left or right):
            self.vl = 0


def main():
    pygame.init()
    size = width, height = 2800, 1752
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    firstwindow_draw()
    pygame.display.set_caption("Chasing the Всеросс")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
