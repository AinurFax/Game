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
                'fish': ['рыбка.png'], 'ramka': ['рамка_зелёная.png', 'рамка_красная.png'],}

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
ramk_group = pygame.sprite.Group()


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
        self.ram = 0
        self.dom = ['домик.png', 'замок.png']

    def add(self, *rect):
        x = 1
        for i in self.rect:
            if i == []:
                break
            i1, i2 = i[0][0], i[0][1]
            if (i1 - rect[0]) ** 2 + (i2 - rect[1]) ** 2 < 250 ** 2:
                x += 1
        self.rect[self.a].append(rect)
        self.rect.append([])
        self.a += 1
        return x

    def dist(self, *pos):
        pygame.draw.circle(screen, pygame.Color('green'), (pos[0] + 30, pos[1] + 30), 200, 2)

    def ramk(self, name):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(name)
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = self.ram
        sprite.rect.y = 850
        ramk_group.add(sprite)
        if self.ram // 100 < 2:
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image(self.dom[self.ram // 100])
            sprite.rect = sprite.image.get_rect()
            if self.ram // 100 == 0:
                sprite.rect.x = self.ram
                sprite.rect.y = 860
            else:
                sprite.rect.x = self.ram
                sprite.rect.y = 850
            ramk_group.add(sprite)
        self.ram += 100

    def update(self, *pos):
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image(self.dom[pos[0][0] // 100])
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = pos[0][0]
        sprite.rect.y = pos[0][1]
        return sprite


k = 0
w = 0
q = 0
level = load_level('levelex1.txt')
level = random_level(level)
level, forest = generate_level(level)
running = True
board = Board()
for _ in range(10):
    board.ramk('рамка_красная.png')
while running:
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    font = pygame.font.Font(None, 20)
    text = font.render(str(k), True, [255, 255, 255])
    textpos = (900, 10)
    screen.blit(text, textpos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if event.pos[0] > 0 and event.pos[1] > 0 and event.pos[0] < 800 and event.pos[1] < 800:
                if q == 1:
                    sprite.rect.x = event.pos[0]
                    sprite.rect.y = event.pos[1]
                    a1 = event.pos[0]
                    a2 = event.pos[1]
                    w = 1
                    pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 0 and event.pos[1] > 0 and event.pos[0] < 800 and event.pos[1] < 800:
                if q == 1:
                    k += board.add(event.pos[0], event.pos[1])
                    pygame.mouse.set_visible(True)
                    q = 0
            if event.pos[0] > 0 and event.pos[1] > 800 and event.pos[0] < 900 and event.pos[1] < 900:
                q = 1
                sprite = board.update(event.pos)
                dom_group.add(sprite)
    if w == 1:
        board.dist(a1, a2)
    ramk_group.draw(screen)
    dom_group.draw(screen)
    pygame.display.flip()
    clock.tick(50)


pygame.quit()