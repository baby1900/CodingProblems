"""
You are given a string of length n and an integer k.
The string can be manipulated by taking one of the first k letters and moving it to the end of the string.

Write a program to determine the lexicographically smallest string that can be created
after an unlimited number of moves.

For example, suppose we are given the string daily and k=1.
The best we can created in this case is ailyd

Solution:
The core point of this solution is that when k >= 2, we can always get the sorted string as out output,
here is the reason:

suppose for xxbaxx with k = 2, the following steps will give us xxabxx back:
1: xxabxx -> abxxxx
2: abxxxx -> bxxxxa
3: bxxxxa -> xxxxab
4: xxxxab -> xxabxx

Thus, when k = 1, we just return the alphabetically earliest rotation if k = 1,
and sorted(string) if k >=2
"""


def det_smallest_rotate_str(input_str, first_letter_range):
    string = list(input_str)

    if first_letter_range == 1:
        best = string
        for i in range(1, len(string)):
            if string[:i] + string[i:] < best:
                best = string[:i] + string[i:]
        return ''.join(best)
    else:
        return ''.join(sorted(input_str))
