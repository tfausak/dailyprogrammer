"""http://redd.it/y26pr

Write a function that calculates the intersection of two rectangles,
returning either a new rectangle or some kind of null value.

You're free to represent these rectangles in any way you want:
tuples of numbers, class objects, new datatypes, anything goes. For
this challenge, you'll probably want to represent your rectangles
as the x and y values of the top-left and bottom-right points.
(Rect(3, 3, 10, 10) would be a rectangle from (3, 3) (top-left) to
(10, 10) (bottom-right).)

As an example, rectIntersection(Rect(3, 3, 10 10), Rect(6, 6, 12,
12)) would return Rect(6, 6, 10, 10), while rectIntersection(Rect(4,
4, 5, 5), Rect(6, 6, 10 10)) would return null.
"""
import sys


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Rectangle(object):
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __str__(self):
        return '({}, {})'.format(self.top_left, self.bottom_right)

    def intersection(self, rectangle):
        top_left = Point(max(self.top_left.x, rectangle.top_left.x),
            max(self.top_left.y, rectangle.top_left.y))
        bottom_right = Point(min(self.bottom_right.x, rectangle.bottom_right.x),
            min(self.bottom_right.y, rectangle.bottom_right.y))
        if top_left.x < bottom_right.x and top_left.y < bottom_right.y:
            return Rectangle(top_left, bottom_right)


def main(args):
    x = Rectangle(Point(3, 3), Point(10, 10))
    y = Rectangle(Point(6, 6), Point(12, 12))
    print x, y, x.intersection(y), y.intersection(x)

    x = Rectangle(Point(4, 4), Point(5, 5))
    y = Rectangle(Point(6, 6), Point(10, 10))
    print x, y, x.intersection(y), y.intersection(x)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
