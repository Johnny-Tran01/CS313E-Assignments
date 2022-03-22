#  File: Hull.py

#  Description: This program will take in multiple points and show the
#  vertices of a convex hull from the left most point going clockwise. It
#  will then show the area of the convex hull.

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/16/2022

#  Date Last Modified: 2/18/2022

import sys
import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (
                abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (
                abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y >= other.y
        return self.x >= other.x


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    return ((p.x * q.y) + (q.x * r.y) + (r.x * p.y) - (p.y * q.x) - (
            q.y * r.x) - (r.y * p.x))


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    # This portion will add the first two points to the upper hull and the
    # first two points to the lower hull
    u_hull = [sorted_points[0], sorted_points[1]]
    l_hull = [sorted_points[-1], sorted_points[-2]]

    # goes through sorted_points and adds the points into either u_hull or
    # l_hull lists.
    for i in range(2, len(sorted_points), 1):
        u_hull.append(sorted_points[i])
        while (len(u_hull) >= 3) and det(u_hull[-3], u_hull[-2], u_hull[-1]) \
                > 0:
            del u_hull[-2]

    for i in range(len(sorted_points) - 3, -1, -1):
        l_hull.append(sorted_points[i])
        while (len(l_hull) >= 3) and det(l_hull[-3], l_hull[-2], l_hull[-1]) \
                > 0:
            del l_hull[-2]

    del l_hull[0]
    del l_hull[-1]
    con_hull = u_hull + l_hull
    return con_hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    sum_1 = 0
    sum_2 = 0

    # these two for loops finds the two sums for the determinant which will
    # then be used to find the area.
    for i in range(len(convex_poly)):
        if i != (len(convex_poly) - 1):
            sum_1 += (convex_poly[i].x * convex_poly[i + 1].y)
        else:
            sum_1 += (convex_poly[i].x * convex_poly[0].y)

    for i in range(len(convex_poly)):
        if i != (len(convex_poly) - 1):
            sum_2 += (convex_poly[i].y * convex_poly[i + 1].x)
        else:
            sum_2 += (convex_poly[i].y * convex_poly[0].x)

    det = sum_1 - sum_2
    return (1/2) * abs(det)


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

    '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

    # get the convex hull
    con_hull = convex_hull(sorted_points)
    # run your test cases

    # print your results to standard output
    print('Convex Hull')
    # print the convex hull
    for i in con_hull:
        print(i)
    # get the area of the convex hull
    area = area_poly(con_hull)
    # print the area of the convex hull
    print()
    print('Area of Convex Hull =', area)


if __name__ == "__main__":
    main()