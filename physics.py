from points import Point
import pygame
import pygame.locals


def force(a, b, r=2):
    """
    :param a: Point A
    :param b: Point B
    :param r: F(x) = 1/|A-B|^r
    :return: Force between points A, B inversely proportional to r'th power
    """
    if type(a) == type(b) == type(Point()):
        return (a - b) / a.distance(b) ** (r + 1)
    else:
        raise ValueError(TypeError, "a and b should belong to class Point")


def visualize(points):
    """
    Program to visualize 2D set of points
    Exit the screen to continue
    :param points: Set of points to be visualized
    :return:
    """
    size = [400, 400]
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    screen.fill(colors['WHITE'])
    pygame.draw.circle(screen, colors['BLACK'], [size[0] / 2, size[1] / 2], size[0] / 4, 5)
    for p in points:
        pygame.draw.circle(screen, colors['RED'], [int(p.coordinates[0] * size[0] / 4) + size[0] / 2,
                                                   int(p.coordinates[1] * size[1] / 4) + size[1] / 2], 5)
    pygame.display.update()

    done = False
    while not done:
        # This will limit the loop to 10 times per sec
        # comment this and program will use all CPU it can
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    pygame.quit()  # being IDLE friendly


colors = {'BLACK': (0, 0, 0),
          'DGREY': (86, 86, 86),
          'LGREY': (172, 172, 172),
          'LRED': (255, 0, 0),
          'RED': (120, 0, 0),
          'GREEN': (0, 255, 0),
          'WHITE': (255, 255, 255),
          'LBLUE': (0, 0, 255),
          'BLUE': (0, 0, 60)
          }
