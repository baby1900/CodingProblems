"""
Given a string and a number of lines k, print the string in zigzag from.

In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line,
then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:
t     a     g
 h   s z   a
  i i   i z
   s     g
"""


def print_spaces(number_space):
    for i in range(number_space):
        print(" ", end="")


def print_zigzag(sentence, line_number):
    n = len(sentence)
    format_arr = [[" " for i in range(n)] for i in range(line_number)]
    y_speed = 1
    space = 0
    line_to_be_print = 0
    for index in range(n):
        format_arr[line_to_be_print][space] = sentence[index]
        if line_to_be_print == line_number - 1:
            y_speed = -1
        elif line_to_be_print == 0:
            y_speed = 1
        line_to_be_print += y_speed
        space += 1
    for i in range(line_number):
        print("".join(format_arr[i]))
