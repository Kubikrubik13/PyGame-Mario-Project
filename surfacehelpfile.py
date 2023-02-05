import pygame


def firstwindow_draw():
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.image('background.png'))

#   Заголовок:
    font = pygame.font.Font(None, 50)
    head_text = font.render("Погоня за всероссом", True, (100, 255, 100))
    head_text_x = 1400 - head_text.get_width() // 2
    head_text_y = 1600 - head_text.get_height() // 2
    screen.blit(head_text, (head_text_x, head_text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 3)

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
