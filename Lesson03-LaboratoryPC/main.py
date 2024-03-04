from Computer import Computer
from Keyboard import Keyboard
from Monitor import Monitor
from Mouse import Mouse
from Order import Order

# CREATE KEYBOARDS
keyboard1 = Keyboard('Bluetooth', 'Logitech')
keyboard2 = Keyboard('Bluetooth', 'Microsoft')
keyboard3 = Keyboard('USB', 'LG')
keyboard4 = Keyboard('USB', 'MagicForce')

# CREATE MOUSES
mouse1 = Mouse('Bluetooth', 'Logitech')
mouse2 = Mouse('USB', 'Asus')
mouse3 = Mouse('Bluetooth', 'Hp')
mouse4 = Mouse('USB', 'Microsoft')

# CREATE MONITORS
monitor1 = Monitor('Dell', 32)
monitor2 = Monitor('LG', 24)
monitor3 = Monitor('Asus', 18)
monitor4 = Monitor('Samsung', 41)

# CREATE COMPUTERS
computer1 = Computer('Apocalypse', monitor1, keyboard1, mouse1)
computer2 = Computer('Rog', monitor2, keyboard2, mouse2)
computer3 = Computer('Omen', monitor3, keyboard3, mouse3)
computer4 = Computer('Alien', monitor4, keyboard4, mouse4)

# CREATE ORDERS
order1 = Order([computer1, computer4])
order2 = Order([computer2])

# PRINTS ORDERS
print('ORDER 1'.center(30, '-'))
print(f'{order1}')
order1.add_computer(computer3)
print(f'{order1}')

print('ORDER 2'.center(30, '-'))
print(f'{order2}')
