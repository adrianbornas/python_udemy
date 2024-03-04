minRange = int(input('What is the min value of the range?: '))
maxRange = int(input('What is the max value of the range?: '))
value = int(input('What is the number to check?: '))

if minRange <= value <= maxRange:
    print(f'The number {value} is between {minRange} and {maxRange}')
else:
    print(f'The number {value} is not between {minRange} and {maxRange}')
