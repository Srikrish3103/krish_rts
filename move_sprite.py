import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 640))


class Sprite:
    def __init__(self, image_path):
        self.image_path = image_path
        self.sprite = pygame.image.load(self.image_path)
        self.pos_x = 0
        self.pos_y = 0

    def update(self):
        window.blit(self.sprite, (self.pos_x, self.pos_y))


class Agent:
    def __init__(self, sprite):
        self.sprite = sprite

    def patrol(self):
        start_point_x = self.pos_x
        start_point_y = self.pos_y
        target_point_x = 100
        target_point_y = 100
        direction_x = target_point_x - start_point_x
        direction_y = target_point_y - start_point_y
        if direction_x > 0:
            self.pos_x += 0.3
        elif direction_x < 0:
            self.pos_x += -1.0 * 0.3
        if direction_y > 0:
            self.pos_y += 0.3
        elif direction_y < 0:
            self.pos_y += -1.0 * 0.3

    def get_next_target_point(self):


run = True
background = Sprite('D:/Game_Pics/rts_background.png')
agent = Agent('D:/Game_Pics/rts_player.png')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    background.update()
    agent.patrol()
    agent.update()
    pygame.display.flip()

pygame.quit()