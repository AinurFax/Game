import os
import sys
import pygame
import time

# Изображение не получится загрузить
# без предварительной инициализации pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    image = load_image('gameover.png')
    rect = image.get_rect()
    rect_x = rect[0]
    rect[0] -= 600
    rect_y = rect[1]
    screen.fill((255, 255, 255))
    screen.blit(image, rect)
    v = 100
    fps = 100
    k = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if k == 0:
            rect = rect.move(rect_x + v // fps, rect_y)
        if rect[0] == 0:
            k = 1
        screen.fill((0, 0, 255))
        screen.blit(image, rect)
        clock.tick(fps)
        pygame.display.flip()

pygame.quit()