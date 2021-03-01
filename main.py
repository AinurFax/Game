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


def urov(a, v, fps, k):
    image = load_image(a)
    rect = image.get_rect()
    rect_x = rect[0]
    rect[0] -= 1000
    rect_y = rect[1]
    screen.fill((255, 255, 255))
    screen.blit(image, rect)
    while True:
        rect = rect.move(rect_x + 10, rect_y)
        if rect[0] == 0:
            break
        screen.fill((0, 0, 0))
        screen.fill((0, 0, 255))
        clock.tick(fps)
        image = load_image('data.png')
        screen.blit(image, (0, 0))
        image = load_image('list.png')
        screen.blit(image, (320, 350))
        image = load_image('avtors.png')
        screen.blit(image, (320, 550))
        image = load_image('ob.png')
        screen.blit(image, (320, 750))
        board.render()
        image = load_image(a)
        screen.blit(image, rect)
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
    global hag, sl, a
    if a == 3:
        if p == -1 and x - 10 > 0:
            if start2 != 0:
                x -= 20
            x -= 10
            if start != 0:
                sliz = "sliz5.png"
            else:
                sliz = "sliz1.png"
            m = 2
            ob.nah('left')
        elif p == 1 and x + 10 < 930:
            if start2 != 0:
                x += 20
            x += 10
            if start != 0:
                sliz = "sliz4.png"
            else:
                sliz = "sliz.png"
            m = 0
            ob.nah('right')
        elif p == -2 and y - 10 > 500:
            if start2 != 0:
                y -= 20
            y -= 10
            ob.nah('hight')
        elif p == 2 and y + 10 < 930:
            if start2 != 0:
                y += 20
            y += 10
            ob.nah('down')
        return x, y, sliz, m
    else:
        if n == 0:
            if p == -1 and x - 10 > 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 < 220:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 > 700:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 < 800:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 1:
            if p == -1 and x - 10 >= 250:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 320:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 670:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 700:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 2:
            if p == -1 and x - 10 >= 390:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 440:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 640:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 3:
            if p == -1 and x - 10 >= 470:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 560:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 590:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 620:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 4:
            if p == -1 and x - 10 >= 590:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 700:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 570:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 590:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 5:
            if p == -1 and x - 10 >= 590:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 680:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 6:
            if p == -1 and x - 10 >= 400:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 7:
            if p == -1 and x - 10 >= 400:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 8:
            if p == -1 and x - 10 >= 200:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 320:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 9:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 10:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 11:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 0:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 12:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 13:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 300:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 14:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 0:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 15:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 0:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 16:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 0:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 17:
            if p == -1 and x - 10 >= 0:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= 0:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        elif n == 18:
            if p == -1 and x - 10 >= -30:
                if start2 != 0:
                    x -= 20
                x -= 10
                if start != 0:
                    sliz = "sliz5.png"
                else:
                    sliz = "sliz1.png"
                m = 2
                ob.nah('left')
            elif p == 1 and x + 10 <= 900:
                if start2 != 0:
                    x += 20
                x += 10
                if start != 0:
                    sliz = "sliz4.png"
                else:
                    sliz = "sliz.png"
                m = 0
                ob.nah('right')
            elif p == -2 and y - 10 >= -30:
                if start2 != 0:
                    y -= 20
                y -= 10
                ob.nah('hight')
            elif p == 2 and y + 10 <= 670:
                if start2 != 0:
                    y += 20
                y += 10
                ob.nah('down')
        return x, y, sliz, m


def prover(x, y, g, m):
    global hag, hop, oby, aaa, start, start1, start2
    if g == 1:
        pass
    elif m == 1:
        if start == 0:
            if x < 730 and x > 650:
                if y < 780 and y > 700:
                    hag = 1000
                    g = 1
                    if oby == 4:
                        oby += 1
                        aaa[2] = 1
                        start2 = time.time()
                        sound2.play()
        else:
            if x < 750 and x > 600:
                if y < 800 and y > 650:
                    hag = 1000
                    g = 1
                    if oby == 4:
                        oby += 1
                        aaa[2] = 1
                        start2 = time.time()
                        sound2.play()
    elif m == 2:
        if start == 0:
            if x < 530 and x > 470:
                if y < 780 and y > 700:
                    hop = 1000
                    g = 1
                    if oby == 3:
                        oby += 1
                        aaa[1] = 1
                        start1 = time.time()
                        sound2.play()
        else:
            if x < 550 and x > 400:
                if y < 800 and y > 650:
                    hop = 1000
                    g = 1
                    if oby == 3:
                        oby += 1
                        aaa[1] = 1
                        start1 = time.time()
                        sound2.play()
    elif m == 3:
        if start == 0:
            if x < 330 and x > 250:
                if y < 780 and y > 700:
                    global sl
                    sl = 1000
                    g = 1
                    if oby == 2:
                        oby += 1
                        aaa[0] = 1
                        start = time.time()
                        y -= 80
                        sound2.play()
    return g, x, y


class Prihok():
    def prov(self, y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites):
        global n
        if stor == 1:
            mm = 0
            sound1.play()
            if a == 3:
                if y - 50 > 500 and x + 50 < 930:
                    y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
            else:
                if n == 0:
                    if y - 50 <= 680 and x + 50 >= 220:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 1:
                    if y - 50 <= 700 and x + 50 >= 320:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 2:
                    if y - 50 <= 680 and x + 50 >= 460:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 3:
                    if y - 50 <= 660 and x + 50 >= 520:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 4:
                    if y - 50 <= 640 and x + 50 >= 600:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 7:
                    if y - 50 <= 640 and x + 50 >= 550:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 11:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 12:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 13:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 15:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 17:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
        else:
            sound1.play()
            mm = 1
            if a == 3:
                if y - 50 > 500 and x - 50 > 0:
                    y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor,
                                                                                  dragon, all_sprites, mm)
            else:
                if n == 5:
                    if y - 50 <= 600 and x - 50 >= 630:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 6:
                    if y - 50 <= 600 and x - 50 >= 520:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 8:
                    if y - 50 <= 600 and x - 50 >= 430:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 9:
                    if y - 50 <= 700 and x - 50 >= 400:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 10:
                    if y - 50 <= 700 and x - 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 14:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
                elif n == 16:
                    if y - 50 <= 700 and x + 50 >= 200:
                        y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prihok(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm)
                        n += 1
        return y, x, g, sliz, sl, hop, prih, dragon, all_sprites

    def prihok(self, y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites, mm):
        if mm == 0:
            all_sprites = pygame.sprite.Group()
            if g[0] == 0:
                all_sprites.add(monet)
            if g[1] == 0:
                all_sprites.add(monet1)
            if g[2] == 0:
                all_sprites.add(monet2)
            if start != 0:
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
                y -= 10
                x += 6
                screen.fill((0, 0, 0))
                screen.blit(image, rect)
                if start != 0:
                    draw(screen, str(round(20 - (time.time() - start), 1)), (100, 200))
                    big.update()
                    all_sprites.add(big)
                if start2 != 0:
                    draw(screen, str(round(20 - (time.time() - start2), 1)), (900, 200))
                    uscor.update()
                    all_sprites.add(uscor)
                if start1 != 0:
                    y -= 20
                    x += 12
                    draw(screen, str(round(20 - (time.time() - start1), 1)), (500, 200))
                    all_sprites.add(znah)
                    znah.update()
                dragon.update()
                dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                clock.tick(fps)
                if a == 1:
                    screen.blit(image1, (150, 700))
                    screen.blit(image1, (270, 660))
                    screen.blit(image1, (390, 620))
                    screen.blit(image1, (510, 580))
                    screen.blit(image1, (630, 540))
                    screen.blit(image1, (510, 500))
                    screen.blit(image1, (390, 460))
                    screen.blit(image1, (510, 420))
                    screen.blit(image1, (390, 380))
                    screen.blit(image1, (270, 340))
                    screen.blit(image1, (150, 300))
                    screen.blit(image1, (270, 260))
                    screen.blit(image1, (390, 220))
                    screen.blit(image1, (510, 180))
                    screen.blit(image1, (390, 120))
                    screen.blit(image1, (510, 80))
                    screen.blit(image1, (390, 40))
                    screen.blit(image1, (510, 0))
                    all_sprites.add(portal)
                    portal.update()
                all_sprites.add(dragon)
                all_sprites.draw(screen)
                pygame.display.flip()
                prih += 1
            prih = 0
            if start != 0:
                sliz = "sliz4.png"
            else:
                sliz = 'sliz.png'
            screen.fill((0, 0, 0))
            screen.blit(image, rect)
            dragon.update()
            dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
            clock.tick(fps)
            if a == 1:
                screen.blit(image1, (150, 700))
                screen.blit(image1, (270, 660))
                screen.blit(image1, (390, 620))
                screen.blit(image1, (510, 580))
                screen.blit(image1, (630, 540))
                screen.blit(image1, (510, 500))
                screen.blit(image1, (390, 460))
                screen.blit(image1, (510, 420))
                screen.blit(image1, (390, 380))
                screen.blit(image1, (270, 340))
                screen.blit(image1, (150, 300))
                screen.blit(image1, (270, 260))
                screen.blit(image1, (390, 220))
                screen.blit(image1, (510, 180))
                screen.blit(image1, (390, 120))
                screen.blit(image1, (510, 80))
                screen.blit(image1, (390, 40))
                screen.blit(image1, (510, 0))
                all_sprites.add(portal)
                portal.update()
            all_sprites.add(dragon)
            all_sprites.draw(screen)
            pygame.display.flip()
        if mm == 1:
            all_sprites = pygame.sprite.Group()
            if g[0] == 0:
                all_sprites.add(monet)
            if g[1] == 0:
                all_sprites.add(monet1)
            if g[2] == 0:
                all_sprites.add(monet2)
            if start != 0:
                sliz = 'sliz6.png'
            else:
                sliz = 'sliz3.png'
            dragon = AnimatedSprite(load_image(sliz), 6, 1, x, y, m)
            while prih != 5:
                y -= 10
                x -= 6
                screen.fill((0, 0, 0))
                screen.blit(image, rect)
                if start != 0:
                    draw(screen, str(round(20 - (time.time() - start), 1)), (100, 200))
                    big.update()
                    all_sprites.add(big)
                if start2 != 0:
                    draw(screen, str(round(20 - (time.time() - start2), 1)), (900, 200))
                    uscor.update()
                    all_sprites.add(uscor)
                if start1 != 0:
                    y -= 20
                    x -= 12
                    draw(screen, str(round(20 - (time.time() - start1), 1)), (500, 200))
                    znah.update()
                    all_sprites.add(znah)
                dragon.update()
                dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
                clock.tick(fps)
                if a == 1:
                    screen.blit(image1, (150, 700))
                    screen.blit(image1, (270, 660))
                    screen.blit(image1, (390, 620))
                    screen.blit(image1, (510, 580))
                    screen.blit(image1, (630, 540))
                    screen.blit(image1, (510, 500))
                    screen.blit(image1, (390, 460))
                    screen.blit(image1, (510, 420))
                    screen.blit(image1, (390, 380))
                    screen.blit(image1, (270, 340))
                    screen.blit(image1, (150, 300))
                    screen.blit(image1, (270, 260))
                    screen.blit(image1, (390, 220))
                    screen.blit(image1, (510, 180))
                    screen.blit(image1, (390, 120))
                    screen.blit(image1, (510, 80))
                    screen.blit(image1, (390, 40))
                    screen.blit(image1, (510, 0))
                    all_sprites.add(portal)
                    portal.update()
                all_sprites.add(dragon)
                all_sprites.draw(screen)
                pygame.display.flip()
                prih += 1
            prih = 0
            if start != 0:
                sliz = "sliz5.png"
            else:
                sliz = 'sliz1.png'
            screen.fill((0, 0, 0))
            screen.blit(image, rect)
            dragon.update()
            dragon.cut_sheet(load_image(sliz), 6, 1, x, y)
            clock.tick(fps)
            if a == 1:
                screen.blit(image1, (150, 700))
                screen.blit(image1, (270, 660))
                screen.blit(image1, (390, 620))
                screen.blit(image1, (510, 580))
                screen.blit(image1, (630, 540))
                screen.blit(image1, (510, 500))
                screen.blit(image1, (390, 460))
                screen.blit(image1, (510, 420))
                screen.blit(image1, (390, 380))
                screen.blit(image1, (270, 340))
                screen.blit(image1, (150, 300))
                screen.blit(image1, (270, 260))
                screen.blit(image1, (390, 220))
                screen.blit(image1, (510, 180))
                screen.blit(image1, (390, 120))
                screen.blit(image1, (510, 80))
                screen.blit(image1, (390, 40))
                screen.blit(image1, (510, 0))
                all_sprites.add(portal)
                portal.update()
            all_sprites.add(dragon)
            all_sprites.draw(screen)
            pygame.display.flip()
        ob.nah('space')
        return y, x, g, sliz, sl, hop, prih, dragon, all_sprites


all_sprites = pygame.sprite.Group()


class Obyh():
    def __init__(self):
        self.left = 0
        self.right = 0
        self.hight = 0
        self.down = 0
        self.space = 0
        self.prov = 0
        self.zel = 0
        self.zel1 = 0
        self.zel2 = 0

    def prover(self):
        if self.left == 1 and self.right == 1 and self.hight == 1 and self.down == 1:
            if self.prov == 0:
                self.prov = 1
                return True
        if self.space == 1:
            if self.prov == 1:
                self.prov = 2
                return True
        if self.zel == 1:
            if self.prov == 2:
                self.prov = 3
                return True
        if self.zel1 == 1:
            if self.prov == 3:
                self.prov = 4
                return True
        if self.zel2 == 1:
            if self.prov == 4:
                self.prov = 5
                return True

    def nah(self, a):
            if a == 'left':
                self.left = 1
            elif a == 'right':
                self.right = 1
            elif a == 'hight':
                self.hight = 1
            elif a == 'space':
                self.space = 1
            else:
                self.down = 1


def draw(screen, name, pos):
    font = pygame.font.Font(None, 50)
    text = font.render(name, True, (100, 255, 100))
    screen.blit(text, pos)


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 300
        self.top = 370
        self.cell_size = 200

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        pass

    def on_click(self, cell):
        return True

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // (self.cell_size * 2)
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        global a
        cell = self.get_cell(mouse_pos)
        if cell:
            if cell[1] == 0:
                return 1
            if cell[1] == 1:
                while running:
                    a = 0
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.pos[0] >= 720 and event.pos[0] <= 740:
                                if event.pos[1] >= 360 and event.pos[1] <= 380:
                                    a = 1
                    if a == 1:
                        break
                    screen.fill((0, 0, 0))
                    image = load_image('data.png')
                    screen.blit(image, (0, 0))
                    image = load_image('list.png')
                    screen.blit(image, (320, 350))
                    image = load_image('avtors.png')
                    screen.blit(image, (320, 550))
                    image = load_image('ob.png')
                    screen.blit(image, (320, 750))
                    board.render()
                    pygame.draw.rect(screen, pygame.Color('white'), (250, 350, 500, 400))
                    image = load_image('Kirp.png')
                    image = pygame.transform.scale(image, (500, 400))
                    screen.blit(image, (250, 350))
                    pygame.draw.line(screen, (0, 255, 0), (720, 360), (740, 380), 5)
                    pygame.draw.line(screen, (0, 255, 0), (720, 380), (740, 360), 5)
                    pygame.display.flip()
            if cell[1] == 2:
                return 3
        else:
            return False


if __name__ == '__main__':
    x = 100
    y = 780
    p = 0
    m = 0
    g = [0, 0, 0]
    prih = 0
    stor = 1
    sliz = "sliz.png"
    hag = 0
    hop = 0
    sl = 0
    ob = Obyh()
    oby = 0
    aaa = [0, 0, 0]
    start = 0
    start1 = 0
    start2 = 0
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    board = Board(1, 3)
    a = False
    pygame.mixer.music.load('saund.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)
    secund = time.time()
    sound1 = pygame.mixer.Sound('pin.mp3')
    sound1.set_volume(0.06)
    sound2 = pygame.mixer.Sound('am.wav')
    sound2.set_volume(0.1)
    Pr = Prihok()
    n = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                a = board.get_click(event.pos)
        screen.fill((0, 0, 0))
        image = load_image('data.png')
        screen.blit(image, (0, 0))
        image = load_image('list.png')
        screen.blit(image, (320, 350))
        image = load_image('avtors.png')
        screen.blit(image, (320, 550))
        image = load_image('ob.png')
        screen.blit(image, (320, 750))
        board.render()
        pygame.display.flip()
        if time.time() - secund >= 191:
            pygame.mixer.music.load('saund.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.05)
            secund = time.time()
        if a == 3:
            break
        if a == 1:
            break
    if a == 3:
        rect, v, fps, k, image = urov('fon.jpg', 100, 100, 0)
    else:
        rect, v, fps, k, image = urov('fon2.png', 100, 100, 0)
        image1 = load_image('plat.png')
        image1 = pygame.transform.scale(image1, (400, 150))
    dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
    monet = AnimatedSprite(load_image('zell.png'), 4, 1, 700, 700, m)
    monet1 = AnimatedSprite(load_image('zell1.png'), 4, 1, 500, 700, m)
    monet2 = AnimatedSprite(load_image('zell2.png'), 4, 1, 300, 700, m)
    obyhen = AnimatedSprite(load_image('obyh.png'), 6, 1, 0, -70, 0)
    big = AnimatedSprite(load_image('big.png'), 2, 1, 0, 100, 0)
    znah = AnimatedSprite(load_image('znah.png'), 2, 1, 200, 100, 0)
    uscor = AnimatedSprite(load_image('uscor.png'), 2, 1, 400, 100, 0)
    portal = AnimatedSprite(load_image('portal.png'), 3, 1, 280, -30, 0)
    all_sprites = pygame.sprite.Group()
    fps = 10
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
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
                    y, x, g, sliz, sl, hop, prih, dragon, all_sprites = Pr.prov(y, x, g, sliz, sl, hop, prih, stor, dragon, all_sprites)
            else:
                p = 0
        if time.time() - secund >= 191:
            pygame.mixer.music.load('saund.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.05)
            secund = time.time()
        screen.fill((0, 0, 0))
        screen.blit(image, rect)
        x, y, sliz, m = perem(x, y, p, sliz, m)
        if p != 0:
            dragon.update()
        else:
            dragon = AnimatedSprite(load_image(sliz), 3, 1, x, y, m)
            all_sprites = pygame.sprite.Group()
        dragon.cut_sheet(load_image(sliz), 3, 1, x, y)
        if a == 3:
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
            g[0], x, y = prover(x, y, g[0], 1)
            g[1], x, y = prover(x, y, g[1], 2)
            g[2], x, y = prover(x, y, g[2], 3)
            if oby == 0:
                if ob.prover():
                    oby += 1
                    obyhen.update()
                all_sprites.add(obyhen)
            elif oby == 1:
                if ob.prover():
                    oby += 1
                    obyhen.update()
                all_sprites.add(obyhen)
            elif oby == 2:
                all_sprites.add(obyhen)
            elif oby == 3:
                if aaa[0] == 1:
                    obyhen.update()
                    aaa[0] = 2
                all_sprites.add(obyhen)
            elif oby == 4:
                if aaa[1] == 1:
                    obyhen.update()
                    aaa[1] = 2
                all_sprites.add(obyhen)
            elif oby == 5:
                if aaa[2] == 1:
                    obyhen.update()
                    aaa[2] = 2
                all_sprites.add(obyhen)
        if start != 0:
            if time.time() - start >= 20:
                start = 0
                y += 80
            else:
                draw(screen, str(round(20 - (time.time() - start), 1)), (100, 200))
                all_sprites.add(big)
                big.update()
        if start1 != 0:
            if time.time() - start1 >= 20:
                start1 = 0
            else:
                draw(screen, str(round(20 - (time.time() - start1), 1)), (500, 200))
                all_sprites.add(znah)
            znah.update()
        if start2 != 0:
            if time.time() - start2 >= 20:
                start2 = 0
            else:
                draw(screen, str(round(20 - (time.time() - start2), 1)), (900, 200))
                all_sprites.add(uscor)
                uscor.update()
        if time.time() - secund >= 191:
            pygame.mixer.music.load('saund.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.05)
            secund = time.time()
        clock.tick(fps)
        if a == 1:
            screen.blit(image1, (150, 700))
            screen.blit(image1, (270, 660))
            screen.blit(image1, (390, 620))
            screen.blit(image1, (510, 580))
            screen.blit(image1, (630, 540))
            screen.blit(image1, (510, 500))
            screen.blit(image1, (390, 460))
            screen.blit(image1, (510, 420))
            screen.blit(image1, (390, 380))
            screen.blit(image1, (270, 340))
            screen.blit(image1, (150, 300))
            screen.blit(image1, (270, 260))
            screen.blit(image1, (390, 220))
            screen.blit(image1, (510, 180))
            screen.blit(image1, (390, 120))
            screen.blit(image1, (510, 80))
            screen.blit(image1, (390, 40))
            screen.blit(image1, (510, 0))
            all_sprites.add(portal)
            portal.update()
            if y <= 10 and y >= -30:
                if x >= 420 and x <= 630:
                    nb = 0
                    while running:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.pos[0] >= 720 and event.pos[0] <= 740:
                                    if event.pos[1] >= 360 and event.pos[1] <= 380:
                                        nb = 1
                        if nb == 1:
                            running = False
                            break
                        screen.fill((0, 0, 0))
                        image = load_image('data.png')
                        screen.blit(image, (0, 0))
                        image = load_image('list.png')
                        screen.blit(image, (320, 350))
                        image = load_image('avtors.png')
                        screen.blit(image, (320, 550))
                        image = load_image('ob.png')
                        screen.blit(image, (320, 750))
                        board.render()
                        image = load_image('kon.png')
                        image = pygame.transform.scale(image, (500, 400))
                        screen.blit(image, (250, 350))
                        pygame.display.flip()
        all_sprites.add(dragon)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()