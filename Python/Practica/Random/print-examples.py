import time

print('Hola', 'mundo!', sep=' - ', end='!!!\n')
print('Hola', 'mundo!', 'este', 'es', 'un', 'ejemplo.')
print('otro,', 'ejemplo.')

print('Footballers:')
print('Ronaldo')
print('Messi')
print('Hazard')
print('Kante')
print('Okocha')

with open('footballers.txt', 'w') as f:
    print('Footballers', end=': ', file=f)
    print('Ronaldo', end=', ', file=f)
    print('Messi', end=', ', file=f)
    print('Hazard', end=', ', file=f)
    print('Kante', end=', ', file=f)
    print('Okocha', file=f) 
    print('Finished writing to file.', file=f)
    print('Check footballers.txt for the output.', file=f)
    

print('Processing...', end=' ', flush=True)
time.sleep(1)
print('Done!')
    