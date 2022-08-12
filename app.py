import pygame

pygame.init()

win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Fireworks")

FPS = 60

colors = [
    (255, 30, 22),
    (38, 250, 27),
    (50, 80, 255),
    (0, 124, 255),
    (255, 124, 0),
    (125, 62, 80),
    (30, 122, 125),
    (90, 124, 200),
    (200, 255, 200),
]


class Projectile:
    pass


class Firework:
    pass


class Launcher:
    WIDTH: 20
    HEIGHT = 20
    COLOR = 'grey'

    def __init__(self ,x ,y, freq) -> None:
        self.x = x
        self.y = y
        self.freq = freq

def main():
    print("main")
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()


def draw():
    win.fill("black")
    pygame.display.update()


if __name__ == "__main__":
    main()
