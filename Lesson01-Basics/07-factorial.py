def factorial(number: int) -> int:
    if number > 1:
        return number * factorial(number-1)
    else:
        return 1


userNumber = int(input('Introduce the number to calculate factorial: '))
result = factorial(userNumber)
print(f'Factorial of {userNumber} is {result}')
