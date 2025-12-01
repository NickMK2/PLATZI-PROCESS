def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia', phone = '1234567890')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia', phone = '1234567890', email = 'azula@gmail.com')