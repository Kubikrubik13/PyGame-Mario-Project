import pygame
import sys
from pygame import Surface
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


width, height = 1200, 600


def firstwindow_draw():
    ## Никаких абсолютных координат, только от width, height
    size = width, height
    screen = pygame.display.set_mode(size)
    screen.blit(load_image('background.png'), [0, 0])

#   Заголовок:
    font = pygame.font.Font(None, 50)
    head_text = font.render("Погоня за всероссом", True, (100, 255, 100))
    head_text_x = width // 2 - head_text.get_width() // 2
    head_text_y = height // 2 - head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))
    pygame.draw.rect(screen, (0, 255, 0), (head_text.get_width() - 10, head_text.get_height() - 10,
                                           head_text_x + 20, head_text_y + 20), 3)

#   Регион:
    font = pygame.font.Font(None, 50)
    head_text = font.render("Регион", True, (100, 255, 100))
    head_text_x = 700 - head_text.get_width() // 2
    head_text_y = 876 + head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))

#   Закл:
    font = pygame.font.Font(None, 50)
    head_text = font.render("Закл", True, (100, 255, 100))
    head_text_x = 2100 - head_text.get_width() // 2
    head_text_y = 876 + head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))

#   Инструкция:
    font = pygame.font.Font(None, 50)
    head_text = font.render('Для уровня "Регион" /n нажмите на левую часть экрана, /n для уровня "Закл" - на правую.',
                            True, (100, 255, 100))
    head_text_x = 2100 - head_text.get_width() // 2
    head_text_y = 876 + head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.MOUSEBUTTONUP[0][0] <= width / 2:
                screen.fill(255, 255, 255)
                