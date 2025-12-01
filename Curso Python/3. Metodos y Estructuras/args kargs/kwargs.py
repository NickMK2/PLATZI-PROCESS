def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_info(name='Carlos', age=30, city='Bogotá')
print_info(name='Carlos', age=30, city='Bogotá', country = 'Colombia')