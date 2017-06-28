#!/usr/bin/env python
def triangle(a, b, c):
    if a == b and b == c:
        return 'Equilateral triangle'
    elif a != b and a != c and b != c:
        return 'Scalene triangle'
    else:
        return 'Isosceles triangle'


if __name__ == '__main__':
    side_a = int(input('Please input triangle side a: '))
    side_b = int(input('Please input triangle side b: '))
    side_c = int(input('Please input triangle side c: '))

    triangle_type = triangle(side_a, side_b, side_c)

    print(triangle_type)
