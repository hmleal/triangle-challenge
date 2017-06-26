#!/usr/bin/env python
def triangle(a, b, c):
    if a == b and b == c:
        return 'Equilateral triangle'
    elif a != b and a != c and b != c:
        return 'Scalene triangle'
    else:
        return 'Isosceles triangle'


if __name__ == '__main__':
    triangle(2, 2, 2)
    triangle(2, 3, 4)

    triangle(2, 2, 3)
    triangle(3, 2, 2)
