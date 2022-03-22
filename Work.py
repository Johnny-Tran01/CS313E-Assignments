#  File: Work.py

#  Description: This program will the user to find the minimum value of v
#  for the given productivity factor that will allow Vyasa to write n lines
#  of code before he sleeps. 

#  Student Name: Johnny Tran

#  Student UT EID: jht825

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 2/19/2022

#  Date Last Modified:

import sys
import time


# this function will give the number of lines Vyasa will need to write
# before falling asleep given v(lines written before coffee) and k(the
# productivity factor)
def number_of_lines(v: int, k: int) -> int:
    lines = v
    p = 1
    # while loop continuously adds lines to lines until k ** p is bigger
    # than or equal to v.
    while v > k ** p:
        lines += v // k ** p
        p += 1
    return lines


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    for i in range(1, n + 1):
        if number_of_lines(i, k) >= n:
            return i
    return 0


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search(n: int, k: int) -> int:
    low = 1
    high = n
    list_1 = list(range(1, n + 1))

    while low <= high:
        mid = (low + high) // 2
        if number_of_lines(list_1[mid], k) == n:
            return list_1[mid]
        elif number_of_lines(list_1[mid], k) >= n:
            high = mid - 1
            list_2 = number_of_lines(list_1[high], k)
            if list_2 < n:
                return list_1[mid]
        elif number_of_lines(list_1[mid], k) < n:
            low = mid + 1
    return 0


# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
