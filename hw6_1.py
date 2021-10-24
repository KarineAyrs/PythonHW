from collections import namedtuple


def calc_dist(gal1, gal2):
    return (((gal1.x - gal2.x) ** 2) + ((gal1.y - gal2.y) ** 2) + ((gal1.z - gal2.z) ** 2)) ** (1 / 2)


def create_galaxies(l):
    Galaxies = namedtuple('Galaxies', ['x', 'y', 'z', 'galaxy'], defaults=[0.0, 0.0, 0.0, ''])
    list_gals = []

    for el in l:
        to_add = el.split()
        list_gals.append(Galaxies(x=float(to_add[0]), y=float(to_add[1]), z=float(to_add[2]), galaxy=str(to_add[3])))

    return sorted(list_gals, key=lambda x: [x.galaxy])


def search_far_galaxy(list_gals):
    max_dist = 0.0
    gal1 = namedtuple('Galaxies', ['x', 'y', 'z', 'galaxy'], defaults=[0.0, 0.0, 0.0, ''])
    gal2 = namedtuple('Galaxies', ['x', 'y', 'z', 'galaxy'], defaults=[0.0, 0.0, 0.0, ''])
    for g1 in list_gals:
        for g2 in list_gals:
            cur_dist = calc_dist(g1, g2)
            if cur_dist > max_dist:
                max_dist = cur_dist
                gal1 = g1
                gal2 = g2

    return list_gals.index(gal1), list_gals.index(gal2)


if __name__ == '__main__':

    n = ''
    l = []
    while n != '.':
        n = input()
        if n != '.':
            l.append(n)
    res = []
    for el in l:
        res.append(el.replace(' ', ','))

    list_gals = create_galaxies(l)

    ind1, ind2 = search_far_galaxy(list_gals)

    if ind1 > ind2:
        print(list_gals[ind2].galaxy, ' ', list_gals[ind1].galaxy)
    else:
        print(list_gals[ind1].galaxy, ' ', list_gals[ind2].galaxy)
