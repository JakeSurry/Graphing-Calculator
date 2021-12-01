from numpy import sign
import func_input
import pygame as pg
pg.init()

SCREEN_SIZE = 800

display = pg.display.set_mode((800,800))
pg.display.set_caption('Calc')

axis_surface = pg.Surface((800, 800))

func_surface = pg.Surface((800, 800))
func_surface.set_colorkey((0, 0, 0))

scale = func_input.scale()
step = 800/scale

def init_axis():
    axis_surface.fill((255, 255, 255))
    for x in range(40):
        if x%5 == 0:
            pg.draw.rect(axis_surface, (150, 150, 150), (x*20, 0, 1, 800))
        else:
            pg.draw.rect(axis_surface, (220, 220, 220), (x*20, 0, 1, 800))

    for y in range(40):
        if y%5 == 0:
            pg.draw.rect(axis_surface, (150, 150, 150), (0, y*20, 800, 1))
        else:
            pg.draw.rect(axis_surface, (220, 220, 220), (0, y*20, 800, 1))

    pg.draw.rect(axis_surface, (0, 0, 0), (400, 0, 1, 800))
    pg.draw.rect(axis_surface, (0, 0, 0), (0, 400, 800, 1))

    return axis_surface

def equal(x, y, func):
        if type(func(x, y)) == bool:
            return func(x, y)

        else:
            amnt = sign(func(x-1/step, y-1/step)) + sign(func(x, y)) + sign(func(x-1/step, y)) + sign(func(x, y-1/step))
            if amnt < 4 and amnt > -4:
                return True

def graph(functions, func):
    #Need this for window to show, guess it's a pygame thing
    for event in pg.event.get():
        pass

    for x in range(800):
        for y in range(800):
            try:
                if equal((x/step)-(scale/2), (scale/2)-(y/step), func):
                    pg.draw.rect(func_surface, functions[func], (x, y, 1, 1))
            except (ValueError, ZeroDivisionError, TypeError) as e:
                pass

        display.blit(axis_surface, (0, 0))
        pg.draw.rect(display, (255, 0, 0), (x, 0, 1, 800))
        display.blit(func_surface, (0, 0))
        pg.display.update()

def main():
    axis_surface = init_axis()

    functions = func_input.get_functions()

    for func in functions:
        graph(functions, func)    

    pg.display.update()

    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        clock.tick(60)

if __name__ == '__main__':
    main()





