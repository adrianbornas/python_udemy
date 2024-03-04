from HerencyMultiple.Rectangle import Rectangle
from HerencyMultiple.Square import Square

print('SQUARE'.center(30, '-'))
mySquare = Square(30, 'red')
print(mySquare)
print(f'AREA: {mySquare.calculate_area()}')

print('\n',)

print('RECTANGLE'.center(30, '-'))
myRectangle = Rectangle(100, 50, 'blue')
print(myRectangle)
print(f'AREA: {myRectangle.calculate_area()}')
