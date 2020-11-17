import sys

import pygame


def run():
    pygame.init()
    pygame.display.set_caption('Pygame测试')
    screen = pygame.display.set_mode((600, 800))
    screen.fill((230, 230, 230))
    screen_rect = screen.get_rect()

    rect_1 = pygame.Rect(10, 10, 15, 15)
    rect_2 = pygame.Rect(20, 10, 10, 20)

    image = pygame.image.load('aeroplane.png')
    rect_plane = image.get_rect()
    rect_plane.x = screen_rect.centerx
    rect_plane.y = screen_rect.centery

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.draw.rect(screen, (1, 1, 1), rect_2)
        pygame.draw.rect(screen, (1, 1, 1), rect_1)
        screen.blit(image, rect_plane)

        pygame.display.flip()


run()
