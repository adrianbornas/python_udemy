print('Insert the following book data:')
bookName: str = input('The book\'s name: ')
bookId: int = int(input('The book\'s ID: '))
bookPrice: float = float(input('The book\'s price: '))
bookShippingCost: bool = input('The shipping cost is free (True/False): ') == 'True'
# Ternary: bookShippingBool: bool = True if bookShippingCost == 'True' else False

print(f'''
    Name: {bookName}
    Id: {bookId}
    Price: {bookPrice}
    Free Shipping: {bookShippingCost}
''')
