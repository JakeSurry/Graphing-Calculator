from numpy import sign, arange, meshgrid, vectorize, stack, where, isfinite
import numpy as np
import func_input
import pygame as pg
import time

class Calculator():
    def __init__(self):

        pg.init()
        pg.font.init()

        self.change_scale(func_input.scale())

        self.recursions = func_input.recursions()

        self.font = pg.font.Font('Cambria.ttf', 20)

        self.display = pg.display.set_mode((800,800))
        pg.display.set_caption('Calc')

        self.axis_surface = self.init_axis()

        self.func_surface = pg.Surface((800, 800))
        self.func_surface.set_colorkey((0, 0, 0))

    def change_scale(self, scale):
        self.scale = scale
        self.step = 800/self.scale

    def init_axis(self):
        axis_surface = pg.Surface((800, 800))

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

        '''
        for num in range(40):
            if num%5 == 0:
                print(self.scale, num)
                self.axis_num((axis_surface, self.scale*(num/40)) - (self.scale/2), num*20+5, 400)
                self.axis_num((axis_surface, self.scale*(num/40)) - (self.scale/2), 405, num*20)
        '''

        pg.draw.rect(axis_surface, (0, 0, 0), (400, 0, 1, 800))
        pg.draw.rect(axis_surface, (0, 0, 0), (0, 400, 800, 1))

        return axis_surface

    '''
    def axis_num(self, axis_surface, num, x, y):
        num_surface = self.font.render(str(num), True, (0, 0, 0))
        axis_surface.blit(num_surface, (x, y))
    '''

    def clear(self):
        self.func_surface.fill((0, 0, 0))
        self.display.blit(self.axis_surface, (0, 0))
        pg.display.update()

    def graph(self, functions, func):
            #Need this for window to show, guess it's a pygame thing
            for k in range(self.recursions):

                for event in pg.event.get():
                    pass

                self.display.blit(self.axis_surface, (0, 0)) 
                pg.display.update()

                xs, ys = meshgrid(arange(-.5, 801), arange(-.5, 801))
                signs0 = sign(func(xs/self.step-self.scale/2, ys/self.step-self.scale/2, k))
                signs1 = signs0[:-1, :-1]
                signs2 = signs0[1:, :-1]
                signs3 = signs0[:-1, 1:]

                grid = where(isfinite(signs1) & ((signs1 != signs2) | (signs1 != signs3)), 1, 0)

                ys, xs = np.where(grid != 0)

                for (x, y) in zip(xs, ys):
                    pg.draw.rect(self.func_surface, functions[func], (x, 800-y, 1, 1))

                self.display.blit(self.func_surface, (0, 0))
                pg.display.update()

            self.recursions = func_input.recursions()
def main():
    calculator = Calculator()

    functions = func_input.get_functions()

    for func in functions:
        calculator.graph(functions, func)    

    clock = pg.time.Clock()
    running = True
    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    calculator.change_scale(calculator.scale * .8)
                    for func in functions:
                        calculator.clear()
                        calculator.graph(functions, func)

                if event.key == pg.K_DOWN:
                    calculator.change_scale(calculator.scale * 1.2)
                    for func in functions:
                        calculator.clear()
                        calculator.graph(functions, func)

        clock.tick(60)

if __name__ == '__main__':
    main()





