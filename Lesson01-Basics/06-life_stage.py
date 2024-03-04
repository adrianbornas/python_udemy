age: int = int(input('How old are you? '))
message: str = ''

if 0 <= age < 10:
    message = 'the childhood is awesome...'
elif 10 <= age < 20:
    message = 'a lot of changes and a lot of study...'
elif 20 <= age < 30:
    message = 'love and work begins...'
else:
    message = 'stage of life don\'t recognised'

print(f'Your age is {age}, {message}')