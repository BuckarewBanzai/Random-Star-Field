import random

def space(arg=None):

    if arg == None:
        seed = random.randint(0, 99999999999999)
        random.seed(seed)
    else:
        seed = arg
        random.seed(seed)

    stars = {':sunny:':1, ':rocket:':1, ':full_moon:':1, ':earth_americas:':1, '✦':20, '　ﾟ':25, '*':30, ',': 35, '.':35, '             ':80}

    field = ''

    for y in range(6):
        for x in range(6):
            for z, q in stars.items():
                if q >= random.randint(0, 100):
                    field += str(z)
                else:
                    field += str('   ')
        field += str('\n\n\n\n\n')

    field += '\nSeed: ' + str(seed)

    print(field)


space(1220035984966)
