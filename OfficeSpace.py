#  File: OfficeSpace.py

#  Description: This program will read in inputs from each employee and
#  output the total space, unallocated space, allocates space, and the space
#  owned by each employee.

#  Student's Name: Johnny Tran

#  Student's UT EID: jht825

#  Partner's Name: Crystal Le

#  Partner's UT EID: cl44964

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/9/2022

#  Date Last Modified:

import sys


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area(rect):
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    height = y2 - y1
    width = x2 - x1

    return height * width


# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap(rect1, rect2):
    # Checks to see if the rectangles are overlapping.
    if rect1[0] >= rect2[2] or rect1[2] <= rect2[0] or rect1[3] <= rect2[1] or \
            rect1[1] >= rect2[3]:
        return 0, 0, 0, 0
    # Compares each point in both rectangles and will return a tuple of
    # overlapping points.
    else:
        if rect2[2] <= rect1[2] and rect2[3] <= rect1[3] and rect2[0] <= rect1[
            0] and rect2[1] <= rect1[1]:
            return rect2[0], rect2[1], rect1[2], rect1[3]
        elif rect1[0] <= rect2[0] and rect1[1] <= rect2[1] and rect1[2] <= \
                rect2[2] and rect1[3] <= rect2[3]:
            return rect2[0], rect2[1], rect1[2], rect1[3]
        elif rect2[0] >= rect1[0] and rect2[1] >= rect1[1] and rect2[2] <= \
                rect1[2] and rect2[3] <= rect1[3]:
            return rect2[0], rect2[1], rect2[2], rect2[3]
        else:
            return rect2[0], rect1[1], rect1[2], rect2[3]


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space(bldg):
    unallocated = 0
    # We check to see if in the 2-D array, if bldg[x][y] is equal 0 then the
    # variable unallocated would add 1.
    for x in range(len(bldg[1])):
        for y in range(len(bldg[0])):
            if bldg[x][y] == 0:
                unallocated += 1
    return unallocated


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space(bldg):
    contested = 0
    # We check to see if in the 2-D array, if bldg[x][y] is greater then the
    # variable contested would add 1.
    for x in range(len(bldg[1])):
        for y in range(len(bldg[0])):
            if bldg[x][y] > 1:
                contested += 1
    return contested


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space(bldg, rect):
    uncontested = 0
    # We check to see if in the 2-D array, if bldg[x][y] is equal 1 then the
    # variable uncontested would add 1.
    for x in range(len(bldg[1])):
        for y in range(len(bldg[0])):
            if bldg[x][y] == 1:
                uncontested += 1
    return uncontested


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space(office, cubicles):
    for i in range(cubicles):
        x_1 = cubicles[0]
        y_1 = cubicles[1]
        x_2 = cubicles[2]
        y_2 = cubicles[3]
        for x in range(x_1, x_2):
            for y in range(y_1, y_2):
                uncontested_space(bldg, (x_1, y_1, x_2, y_2))


#  Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    assert area((0, 0, 1, 1)) == 1

    # write your own test cases

    return "all test cases passed"


def main():
    # read the data
    dimensions = sys.stdin.readline().split()
    bldg = [[0 for h in range(int(dimensions[0]))] for w in range(
        int(dimensions[1]))]
    num_employees = sys.stdin.readline().strip()
    employee_list = []
    for i in range(len(num_employees)):
        employee_list.append(sys.stdin.readline().split())

    # run your test cases
    '''
  print (test_cases())
  '''
    # print the following results after computation
    # compute the total office space
    sys.stdout.write('Total', )
    # compute the total unallocated space
    sys.stdout.write('Unallocated', )
    # compute the total contested space
    sys.stdout.write('Contested', )
    # compute the uncontested space that each employee gets
    for i in range(len(num_employees)):
        sys.stdout.write(str(employee_list[0]), )


if __name__ == "__main__":
    main()
