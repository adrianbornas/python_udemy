from Basics.Rectangle import Rectangle
from Basics.ArithmeticOperations import ArithmeticOperations

# ------------------------
print(f'RECTANGLE AREA'.center(30, '-'))
base = float(input('Introduce the rectangle\'s base: '))
height = float(input('Introduce the rectangle\'s height: '))

myRectangle = Rectangle(base, height)
print(f'Area of rectangle is {myRectangle.calculate_area()}')

# ------------------------
print(f'ARITHMETICS OPERATIONS'.center(30, '-'))
myCalculator = ArithmeticOperations()

myCalculator.numbers = [1, 2, 3, 4, 5]
print(f'Sum: {myCalculator.sum()}')

myCalculator.numbers = [1, 2]
print(f'Subtraction: {myCalculator.subtraction()}')

myCalculator.numbers = [1, 2, 3, 4, 5]
print(f'Multiplication: {myCalculator.multiplication()}')

myCalculator.numbers = [1, 2]
print(f'Division: {myCalculator.division():.2f}')
