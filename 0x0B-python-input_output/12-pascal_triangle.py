#!/usr/bin/python3
def pascal_triangle(n):
    """ Function that returns the pascal triangle
    Args:
        n: number of lines
    Returns:
        array: an array with the pascal triangle
    """

    array = []
    prev = []

    for i in range(n):
        res_list = []
        pasc_1 = -1
        pasc_2 = 0
        for j in range(len(prev) + 1):
            if pasc_1 == -1 or pasc_2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[pasc_1] + prev[pasc_2]]
            pasc_1 += 1
            pasc_2 += 1
        array.append(res_list)
        prev = res_list[:]

    return array
