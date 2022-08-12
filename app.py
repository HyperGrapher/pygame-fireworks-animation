from pickle import TRUE
import time
import pygame

pygame.init()
WIN_HEIGHT = 720
WIN_WIDTH = 1280
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Fireworks")

FPS = 60

colors = [
    (255, 30, 22),
    (38, 250, 90),
    (50, 80, 255),
    (0, 124, 255),
    (255, 124, 0),
    (125, 180, 180),
    (30, 250, 125),
    (90, 124, 200),
    (200, 255, 200),
    (240, 27, 80),
]


class Projectile:
    pass


class Firework:
    RAD = 10
    MAX_PROJECTILES = 270
    MIN_PROJECTILES = 80
    PROJECTILE_VEL = 4

    def __init__(self, x, y, y_vel, explode_height, color) -> None:
        self.x = x
        self.y = y
        self.y_vel = y_vel
        self.explode_height = explode_height
        self.color = color
        self.exploded = False
        self.projectiles = []

    def explode(self):
        self.exploded = TRUE
        

    def move(self, max_w, max_h):
        if not self.exploded:
            self.y += self.y_vel

            if self.y >= self.explode_height:
                self.explode()

    
    def draw(self, win):
        if not self.exploded:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.RAD)

        for projectile in self.projectiles:
            projectile.draw(win)

class Launcher:
    WIDTH = 20
    HEIGHT = 20
    COLOR = "grey"

    def __init__(self, x, y, freq) -> None:
        self.x = x
        self.y = y
        self.freq = freq
        self.start_time = time.time()
        self.firewors = []

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def launch(self):
        pass

    def loop(self, max_w, max_h):
        current_t = time.time()
        t_elapsed = current_t - self.start_time

        if t_elapsed * 1000 >= self.freq:
            self.start_time = current_t
            self.launch()


def main():
    print("main")
    run = True
    clock = pygame.time.Clock()

    launchers = [Launcher(20, WIN_HEIGHT, 60)]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(launchers)


def draw(launchers: list[Launcher]):
    win.fill(colors[4])

    for lan in launchers:
        lan.draw(win)

    pygame.display.update()


if __name__ == "__main__":
    main()
