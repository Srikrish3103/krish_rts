import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 640))


class Agent:
    def __init__(self, image_path, color, pos_x, pos_y):
        self.image_path = image_path
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.team_color = pygame.Surface(self.sprite.get_size()).convert_alpha()
        self.team_color.fill(color)
        self.pos_x = pos_x
        self.pos_y = pos_y

    # def patrol(self):
    #     self.sprite.move(200, 200)

    def draw(self):
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_size()[0] * 0.2, self.sprite.get_size()[1] * 0.2))
        self.sprite.blit(self.team_color, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        window.blit(self.sprite, (self.pos_x, self.pos_y))


run = True
agents = []

# Team1
for i in range(0, 5):
    r = 255
    g = 0
    b = 0
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    agent = Agent('D:/Game_Pics/rts_player.png', pygame.Color(r, g, b), x, y)
    #agent.patrol()
    agents.append(agent)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for agent in agents:
        agent.draw()
    pygame.display.flip()

pygame.quit()