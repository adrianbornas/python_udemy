from custom_user import CustomUser
from custom_user_dao import CustomUserDao
from logger_base import log

option = ''

while option != '5':
    print('1) List users')
    print('2) Add user')
    print('3) Update user')
    print('4) Delete user')
    print('5) Exit')
    option = input('> ')
    print('\n')

    if option == '1':
        log.info(f'USERS'.center(30, '-'))
        result = CustomUserDao.select()
        for row in result:
            log.info(row)
        print(''.center(30, '-'))
    elif option == '2':
        username = input('Username: ')
        password = input('Password: ')
        user = CustomUser(username=username, password=password)
        result = CustomUserDao.insert(user)
        log.info(f'Inserted {result} rows')
        print(''.center(30, '-'))
    elif option == '3':
        id_user = int(input('Id of user to update: '))
        username = input('Username: ')
        password = input('Password: ')
        user = CustomUser(id_user=id_user, username=username, password=password)
        result = CustomUserDao.update(user)
        log.info(f'Updated {result} rows')
        print(''.center(30, '-'))
    elif option == '4':
        id_user = int(input('Id of user to delete: '))
        user = CustomUser(id_user=id_user)
        result = CustomUserDao.delete(user)
        log.info(f'Deleted {result} rows')
        print(''.center(30, '-'))

print('EXIT'.center(30, '-'))
