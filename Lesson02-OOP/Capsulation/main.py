from Capsulation.Cube import Cube

width = float(input('Width of the cube: '))
depth = float(input('Depth of the cube: '))
height = float(input('Height of the cube: '))

myCube = Cube(width, depth, height)

if __name__ == '__main__':
    print(f'Cube\'s volume is {myCube.calculate_volume()}')

del myCube
