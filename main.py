import os
import sys
import pygame

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


def urov(a, v, fps, k):
    image = load_image(a)
    rect = image.get_rect()
    rect_x = rect[0]
    rect[0] -= 1000
    rect_y = rect[1]
    screen.fill((255, 255, 255))
    screen.blit(image, rect)
    while True:
        rect = rect.move(rect_x + v // fps, rect_y)
        if rect[0] == 0:
            break
        screen.fill((0, 0, 255))
        screen.blit(image, rect)
        clock.tick(fps)
        pygame.display.flip()
    return rect, v, fps, k, image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, m):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows, x, y)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows, x, y):
        self.rect = pygame.Rect(x, y, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def perem(x, y, p, sliz, m):
    if p == -1 and x - 10 > 0:
        x -= 10
        sliz = "sliz1.png"
        m = 2
    elif p == 1 and x + 10 < 930:
        x += 10
        sliz = "sliz.png"
        m = 0
    elif p == -2 and y - 10 > 500:
        y -= 10
    elif p == 2 and y + 10 < 930:
        y += 10
    return x, y, sliz, m


def prover(x, y, g):
    if g == 1:
        pass
    elif x < 710 and x > 650:
        if y < 670 and y > 630:
            print('Ваня')
            g = 1
        else:
            pass
    else:
        pass
    return g


all_sprites = pygame.sprite.Group()


if __name__ == '__main__':
    x = 100
    y = 600
    p = 0
    m = 0
    g = 0
    prih = 0
    stor = 1
    sliz = "sliz.png"
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    rect, v, fps, k, image = urov('fon.jpg', 100, 100, 0)
    running = True
    dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
    monet = AnimatedSprite(load_image('coin.png'), 6, 1, 700, 700, m)
    all_sprites = pygame.sprite.Group()
    fps = 10
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p = -1
                    stor = 0
                elif event.key == pygame.K_RIGHT:
                    p = 1
                    stor = 1
                elif event.key == pygame.K_UP:
                    p = -2
                elif event.key == pygame.K_DOWN:
                    p = 2
                elif event.key == pygame.K_SPACE:
                    if stor == 1:
                        if y - 50 > 500 and x + 50 < 930:
                            all_sprites = pygame.sprite.Group()
                            if g != 1:
                                all_sprites.add(monet)
                            sliz = 'sliz2.png'
                            dragon = AnimatedSprite(load_image(sliz), 6, 1, x, y, m)
                            while prih != 5:
                                y -= 10
                                x += 6
                                screen.fill((0, 0, 0))
                                screen.blit(image, rect)
                                dragon.update()
                                dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                                all_sprites.add(dragon)
                                all_sprites.draw(screen)
                                clock.tick(fps)
                                pygame.display.flip()
                                prih += 1
                            prih = 0
                        sliz = 'sliz.png'
                        screen.fill((0, 0, 0))
                        screen.blit(image, rect)
                        dragon.update()
                        dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                        all_sprites.add(dragon)
                        all_sprites.draw(screen)
                        clock.tick(fps)
                        pygame.display.flip()
                    else:
                        if y - 50 > 500 and x - 50 > 0:
                            all_sprites = pygame.sprite.Group()
                            if g != 1:
                                all_sprites.add(monet)
                            sliz = 'sliz3.png'
                            dragon = AnimatedSprite(load_image(sliz), 6, 1, x, y, m)
                            while prih != 5:
                                y -= 10
                                x -= 6
                                screen.fill((0, 0, 0))
                                screen.blit(image, rect)
                                dragon.update()
                                dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                                all_sprites.add(dragon)
                                all_sprites.draw(screen)
                                clock.tick(fps)
                                pygame.display.flip()
                                prih += 1
                            prih = 0
                        sliz = 'sliz1.png'
                        screen.fill((0, 0, 0))
                        screen.blit(image, rect)
                        dragon.update()
                        dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                        all_sprites.add(dragon)
                        all_sprites.draw(screen)
                        clock.tick(fps)
                        pygame.display.flip()
            else:
                p = 0
        screen.fill((0, 0, 0))
        screen.blit(image, rect)
        x, y, sliz, m = perem(x, y, p, sliz, m)
        if p != 0:
            dragon.update()
        else:
            dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
            all_sprites = pygame.sprite.Group()
        dragon.cut_sheet(load_image(sliz), 3, 1, x, y)
        if g != 1:
            monet.cut_sheet(load_image('coin.png'), 6, 1, 700, 700)
            monet.update()
            all_sprites.add(monet)
        g = prover(x, y, g)
        clock.tick(fps)
        all_sprites.add(dragon)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()