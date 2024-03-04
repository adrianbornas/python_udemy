from io import TextIOWrapper

# Handle file manually
file = None
try:
    file = open('trial.txt', 'w', encoding='utf8')
    file.write('Hello world!\n')
    file.write('Goodbye')
except Exception as error:
    print(f'EXCEPTION: {type(error)} - {error}')
finally:
    if isinstance(file, TextIOWrapper):
        file.close()
