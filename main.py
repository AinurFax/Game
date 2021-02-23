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
    global hag, sl
    if p == -1 and x - 10 > 0:
        if hag != 0:
            hag -= 1
            x -= 20
        x -= 10
        if sl - 1 > 0:
            sliz = "sliz5.png"
        else:
            sliz = "sliz1.png"
        m = 2
    elif p == 1 and x + 10 < 930:
        if hag != 0:
            hag -= 1
            x += 20
        x += 10
        if sl - 1 > 0:
            sliz = "sliz4.png"
        else:
            sliz = "sliz.png"
        m = 0
    elif p == -2 and y - 10 > 500:
        if hag != 0:
            hag -= 1
            y -= 20
        y -= 10
    elif p == 2 and y + 10 < 930:
        if hag != 0:
            hag -= 1
            y += 20
        y += 10
    return x, y, sliz, m


def prover(x, y, g, m):
    global hag, hop
    if g == 1:
        pass
    elif m == 1:
        if x < 710 and x > 670:
            if y < 760 and y > 720:
                hag = 100
                g = 1
            else:
                pass
    elif m == 2:
        if x < 510 and x > 470:
            if y < 760 and y > 720:
                hop = 100
                g = 1
            else:
                pass
    elif m == 3:
        if x < 310 and x > 270:
            if y < 760 and y > 720:
                global sl
                sl = 1000
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
    g = [0, 0, 0]
    prih = 0
    stor = 1
    sliz = "sliz.png"
    hag = 0
    hop = 0
    sl = 0
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    rect, v, fps, k, image = urov('fon.jpg', 100, 100, 0)
    running = True
    dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
    monet = AnimatedSprite(load_image('zell.png'), 4, 1, 700, 700, m)
    monet1 = AnimatedSprite(load_image('zell1.png'), 4, 1, 500, 700, m)
    monet2 = AnimatedSprite(load_image('zell2.png'), 4, 1, 300, 700, m)
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
                            if g[0] == 0:
                                all_sprites.add(monet)
                            if g[1] == 0:
                                all_sprites.add(monet1)
                            if g[2] == 0:
                                all_sprites.add(monet2)
                            if sl - 1 > 0:
                                sliz = 'sliz7.png'
                            else:
                                sliz = 'sliz2.png'
                            dragon = AnimatedSprite(load_image(sliz), 6, 1, x, y, m)
                            while prih != 5:
                                if g[0] == 0:
                                    monet.update()
                                if g[1] == 0:
                                    monet1.update()
                                if g[2] == 0:
                                    monet2.update()
                                if hop - 1 > 0:
                                    hop -= 1
                                    y -= 20
                                    x += 12
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
                        if sl - 1 > 0:
                            sliz = "sliz4.png"
                        else:
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
                            if g[0] == 0:
                                all_sprites.add(monet)
                            if g[1] == 0:
                                all_sprites.add(monet1)
                            if g[2] == 0:
                                all_sprites.add(monet2)
                            if sl - 1 > 0:
                                sliz = 'sliz6.png'
                            else:
                                sliz = 'sliz3.png'
                            dragon = AnimatedSprite(load_image(sliz), 6, 1, x, y, m)
                            while prih != 5:
                                if hop - 1 > 0:
                                    hop -= 1
                                    y -= 20
                                    x -= 12
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
                        if sl - 1 > 0:
                            sliz = "sliz5.png"
                        else:
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
        if sl - 1 > 0:
            sl -= 1
        screen.fill((0, 0, 0))
        screen.blit(image, rect)
        x, y, sliz, m = perem(x, y, p, sliz, m)
        if p != 0:
            dragon.update()
        else:
            dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
            all_sprites = pygame.sprite.Group()
        dragon.cut_sheet(load_image(sliz), 3, 1, x, y)
        if g[0] == 0:
            monet.cut_sheet(load_image('zell.png'), 4, 1, 700, 700)
            monet.update()
            all_sprites.add(monet)
        if g[1] == 0:
            monet1.cut_sheet(load_image('zell1.png'), 4, 1, 500, 700)
            monet1.update()
            all_sprites.add(monet1)
        if g[2] == 0:
            monet2.cut_sheet(load_image('zell2.png'), 4, 1, 250, 700)
            monet2.update()
            all_sprites.add(monet2)
        g[0] = prover(x, y, g[0], 1)
        g[1] = prover(x, y, g[1], 2)
        g[2] = prover(x, y, g[2], 3)
        clock.tick(fps)
        all_sprites.add(dragon)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()