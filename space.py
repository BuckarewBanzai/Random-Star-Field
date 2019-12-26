import random

stars = {':sunny:':1, ':rocket:':1, ':full_moon:':1, ':earth_americas:':1, '✦':20, '　ﾟ':30, '*':40, ',': 50, '.':60, '             ':70}

key = random.choice(list(stars))
for y in range(10):
    for x in range(10):
        for z, q in stars.items():
            if q >= random.randint(0, 100):
                print(z, end='')
            else:
                print('    ', end='')
    print("\n")
