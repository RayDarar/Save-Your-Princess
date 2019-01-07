import pygame

class Bullet:
    def __init__(self):
        self.coords = (0, 250)
        self.speed = 5
    pass

def Start():
    pygame.init();
    screen = pygame.display.set_mode((500, 500))
    running = True

    bullets = list()

    while running:
        pygame.time.Clock().tick(30)
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_e]):
            if (len(bullets) <= 5):
                bullets.append(Bullet())

        for event in pygame.event.get():
            if (event.type == pygame.QUIT): running = False
            pass
        for bullet in bullets:
            bullet.coords = (bullet.coords[0] + bullet.speed, bullet.coords[1])
            if (bullet.coords[0] >= 500):
                bullets.remove(bullet)
            pass

        for obj in bullets:
            pygame.draw.circle(screen, (255, 255, 255), obj.coords, 6)
            pass
        pygame.display.update()
        pass
    pygame.quit()
    pass