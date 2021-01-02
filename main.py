import pygame
import sys
import os
from random import choice

FPS = 50
pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


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


def load_level(filename):
    fullname = os.path.join('data', filename)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png'), 'water': load_image('woda.jpg')}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
dom_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            else:
                Tile('water', x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, level, x, y


def random_level(level1):
    level2 = [[]]
    a = 0
    s = choice(['#', '.', '@'])
    for i in range(len(level1)):
        for j in range(len(level1)):
            if a == 5 and j % 8 == 0:
                s = choice(['#', '.', '@'])
                a = 0
            level2[i].append(s)
        level2.append([])
        a += 1
    return level2


level = load_level('levelex1.txt')
level = random_level(level)
generate_level(level)
running = True
sprite = pygame.sprite.Sprite()
sprite.image = load_image("dom.jpg")
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 200
sprite.rect.y = 20
dom_group.add(sprite)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    dom_group.draw(screen)
    pygame.display.flip()
    clock.tick(50)


pygame.quit()
