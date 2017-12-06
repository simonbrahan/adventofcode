from math import sqrt, ceil, fmod
from sys import argv

def find_ulam_layer(num):
    """ Given a number
        find the layer of the ulam spiral

        The layer is defined as the half-square section
        in which the number appears

        so:
            1 is on layer 0
            2, 3 and 4 are on layer 0
            5, 6, 7, 8 and 9 are on layer 0
            etc
    """
    return int(ceil(sqrt(num))) - 1


def find_ulam_layer_square(layer_num):
    """ Given an ulam layer number
        find the layer square the layer sits on

        so:
            0 is on square 0
            1 is on square 1
            2 is on square 1
            3 is on square 2
            etc
    """
    return int(ceil(layer_num / 2.0))


def find_ulam_layer_parity(layer_num):
    """ Given an ulam layer number
        find the direction in which the layer is "drawn"

        so:
            0 is given the parity -1
            1 is given the parity 1
            2 is given the perity -1
            etc
    """
    return [-1, 1][int(fmod(layer_num, 2))]


def find_ulam_layer_start(layer_num):
    """ Given an ulam layer number
        find the first number on the layer

        so:
            0 starts with 1
            1 starts with 2
            2 starts with 5
            3 starts with 10
            etc
    """
    return layer_num ** 2 + 1


def find_ulam_layer_corner(layer_num):
    """ Given an ulam layer number
        find the value of the corner on that layer

        so:
            0 gives 1
            1 gives 3
            2 gives 7
            3 gives 13
            etc
    """
    return find_ulam_layer_start(layer_num) + layer_num


def find_ulam_coords(num):
    """ Given a number
        find the coordinates of that number on the ulam spiral

        so:
            1 gives [0, 0]
            2 gives [1, 0]
            18 gives [-2, 1]
            etc
    """
    layer_num = find_ulam_layer(num)
    layer_square = find_ulam_layer_square(layer_num)
    layer_parity = find_ulam_layer_parity(layer_num)
    layer_start = find_ulam_layer_start(layer_num)
    layer_corner = find_ulam_layer_corner(layer_num)

    """
        Start with layer corner coordinates
        As layers are defined as "half squares" of the spiral,
        the corner will be either "north east" or "south west"
    """
    corner_coords = [
        layer_parity * layer_square,
        layer_parity * layer_square
    ]

    if num < layer_corner:
        return corner_coords
    elif num > layer_corner:
        return corner_coords
    else:
        return corner_coords


print find_ulam_coords(int(argv[1]))
