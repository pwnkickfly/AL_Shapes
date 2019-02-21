import math
from Box import Box
from Pyramid import Pyramid
from Sphere import Sphere

class ShapeTester:
    print('welcome to Shape Tester')
    print('Please choose \'box\', \'pyramid\', or \'sphere\'')
    while True:
        shape = input('>')
        if shape == 'box':
            print('You Chose Box')
            width = int(input('choose a width: '))
            height = int(input('choose a height: '))
            length = int(input('choose a length: '))
            b1 = Box(length, width, height)
            print('The Volume is: %f' % b1.getVolume())
            print('The Surface Area is %f' % b1.getSurfArea())
        elif shape == 'pyramid':
            print('You Chose Pyramid')
            width = int(input('choose a width: '))
            height = int(input('choose a height: '))
            length = int(input('choose a length: '))
            p1 = Pyramid(length, width, height)
            print('The Volume is: %f' % p1.getVolume())
            print('The Surface Area is %f' % p1.getSurfArea())
        elif shape == 'sphere':
            print('You Chose Sphere')
            radius = int(input('choose a radius: '))
            s1 = Sphere(radius)
            print('The Volume is: %f' % s1.getVolume())
            print('The Surface Area is: %f' % s1.getSurfArea())
        else:
            print('incorrect syntax try again')
