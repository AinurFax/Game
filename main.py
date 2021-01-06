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


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.png'), 'water': load_image('woda.jpg'),
               'forest': ['дерево.png', 'дуб.png', 'недуб.png', 'дуб.png', 'недуб.png', 'дуб.png', 'недуб.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png',
                          'дуб.png', 'недуб.png', 'яблоня.png', 'дуб.png', 'недуб.png', 'яблоня.png'],
               'desert': ['кактус.png', 'кактусмини.png'],
                'fish': ['рыбка.png']}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'forest':
            self.image = load_image(choice(tile_images[tile_type]))
        elif tile_type == 'desert':
            self.image = load_image(choice(tile_images[tile_type]))
        elif tile_type == 'fish':
            self.image = load_image(choice(tile_images[tile_type]))
        else:
            self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
dom_group = pygame.sprite.Group()


def generate_level(level):
    forest = False
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '!':
                Tile('empty', x, y)
                Tile('forest', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('water', x, y)
            elif level[y][x] == '+':
                Tile('wall', x, y)
                Tile('desert', x, y)
            elif level[y][x] == '-':
                Tile('water', x, y)
                Tile('fish', x, y)
    return level, forest


def random_level(level1):
    level2 = [[]]
    q = 0
    s = choice(['#', '.', '@'])
    a = choice([1, 2, 3, 4, 5, 6])
    b = choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])
    b1 = choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    b2 = choice([2, 3, 4, 5, 6, 7, 8, 9, 10])
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    for i in range(len(level1)):
        for j in range(len(level1)):
            if q == 5 and j % 8 == 0:
                s = choice(['#', '.', '@'])
                q = 0
            if s == '.':
                a3 = 0
                a4 = 0
                a5 = 0
                a6 = 0
                if a1 == a:
                    if a2 != b:
                        a = choice([1, 2, 3, 4, 5, 6])
                        a2 += 1
                        level2[i].append('!')
                        a1 = 0
                    else:
                        level2[i].append(s)
                        a1 += 1
                else:
                    level2[i].append(s)
                    a1 += 1
            elif s == '#':
                a2 = 0
                a1 = 0
                a5 = 0
                a6 = 0
                if a3 == a:
                    if a4 != b1:
                        a = choice([1, 2, 3, 4, 5, 6])
                        a4 += 1
                        level2[i].append('+')
                        a3 = 0
                    else:
                        level2[i].append(s)
                        a3 += 1
                else:
                    level2[i].append(s)
                    a3 += 1
            elif s == '@':
                a3 = 0
                a4 = 0
                a2 = 0
                a1 = 0
                if a5 == a:
                    if a6 != b2:
                        a = choice([1, 2, 3, 4, 5, 6])
                        a6 += 1
                        level2[i].append('-')
                        a5 = 0
                    else:
                        level2[i].append(s)
                        a5 += 1
                else:
                    level2[i].append(s)
                    a5 += 1
        level2.append([])
        q += 1
    return level2


class Board:
    def __init__(self):
        self.rect = [[]]
        self.a = 0

    def add(self, *rect):
        x = 0
        for i in self.rect:
            if i == []:
                break
            i1, i2 = i[0][0], i[0][1]
            if i1 + 100 > rect[0] and i1 - 100 < rect[0]:
                x += 1
            elif i2 + 100 > rect[1] and i2 - 100 < rect[1]:
                x += 1
        self.rect[self.a].append(rect)
        self.rect.append([])
        self.a += 1
        if x == 0:
            x = 1
        return x


k = 0
level = load_level('levelex1.txt')
level = random_level(level)
level, forest = generate_level(level)
running = True
sprite = pygame.sprite.Sprite()
sprite.image = load_image("dom.png")
sprite.rect = sprite.image.get_rect()
dom_group.add(sprite)
board = Board()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if event.pos[0] - 30 > 0 and event.pos[1] - 30 > 0 and event.pos[0] - 30 < 800 and event.pos[1] - 30 < 800:
                sprite.rect.x = event.pos[0] - 30
                sprite.rect.y = event.pos[1] - 30
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] - 30 > 0 and event.pos[1] - 30 > 0 and event.pos[0] - 30 < 800 and event.pos[1] - 30 < 800:
                sprite.rect.x = event.pos[0] - 30
                sprite.rect.y = event.pos[1] - 30
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image("dom.png")
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = event.pos[0] - 30
                sprite.rect.y = event.pos[1] - 30
                k += board.add(event.pos[0] - 30, event.pos[1] - 30)
                dom_group.add(sprite)
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    dom_group.draw(screen)
    font = pygame.font.Font(None, 20)
    text = font.render(str(k), True, [255, 255, 255])
    textpos = (900, 10)
    screen.blit(text, textpos)
    pygame.display.flip()
    clock.tick(50)


pygame.quit()