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
        rect = rect.move(rect_x + v // fps, rect_y)
        if rect[0] == 0:
            break
        screen.fill((0, 0, 255))
        screen.blit(image, rect)
        clock.tick(fps)
        pygame.display.flip()
    return rect, v, fps, k, image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


all_sprites = pygame.sprite.Group()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    rect, v, fps, k, image = urov('fon.jpg', 100, 100, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(image, rect)
        clock.tick(fps)
        dragon = AnimatedSprite(load_image("a.png"), 8, 2, 50, 50)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()