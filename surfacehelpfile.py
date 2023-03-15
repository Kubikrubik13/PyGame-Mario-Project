import pygame
import sys
from pygame import Surface
from const import WIDTH, HEIGHT
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def firstwindow_draw():
    ## Никаких абсолютных координат, только от WIDTH, HEIGHT

    pygame.init()
    running = True
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    image_bg = load_image('background.png')
    BG_IMAGE_SIZE = (WIDTH, HEIGHT)
    image_bg = pygame.transform.scale(image_bg, BG_IMAGE_SIZE)
    screen.blit(image_bg, [0, 0])

    #   Заголовок:
    font = pygame.font.Font(None, 50)
    head_text_mid = font.render("Погоня за всероссом", True, (100, 255, 100))
    head_text_x = WIDTH // 2 - head_text_mid.get_width() // 2
    head_text_y = HEIGHT // 2
    screen.blit(head_text_mid, (head_text_x, head_text_y))
    pygame.draw.rect(screen, (0, 255, 0), (head_text_mid.get_width() - 10, head_text_mid.get_height() - 10,
                                           head_text_x + 20, head_text_y + 20), 3)

    #   Регион:
    font = pygame.font.Font(None, 50)
    head_text_lf = font.render("Регион", True, (100, 255, 100))
    head_text_x = (WIDTH // 2) // 4
    head_text_y = HEIGHT // 2 + head_text_lf.get_height() // 2 - 20
    screen.blit(head_text_lf, (head_text_x, head_text_y))

    #   Закл:
    font = pygame.font.Font(None, 50)
    head_text_rg = font.render("Закл", True, (100, 255, 100))
    head_text_x = (WIDTH // 2) * 55 // 32
    head_text_y = HEIGHT // 2 + head_text_rg.get_height() // 2 - 20
    screen.blit(head_text_rg, (head_text_x, head_text_y))

    #   Инструкция:
    font = pygame.font.Font(None, 50)
    head_text = font.render('Для уровня "Регион" /n нажмите на левую часть экрана, /n для уровня "Закл" - на правую.',
                            True, (100, 255, 100))
    head_text_x = 2100 - head_text.get_width() // 2
    head_text_y = 876 + head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))

    return lvl

firstwindow_draw()
