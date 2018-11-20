# Let A[0...n - 1] be an array of n distinct positive integers.
# If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A.
# Given n and an array A your task is to find the number of inversions of A.

# Input
# The first line contains t, the number of testcases followed by a blank space.
# Each of the t tests start with a number n (n <= 200000). Then n + 1 lines follow.
# In the ith line a number A[i - 1] is given (A[i - 1] <= 10^7).
# The (n + 1)th line is a blank space.

# Output
# For every test output one line giving the number of inversions of A.


def countLessAndEq(arg):
    count = 0
    while(arg > 0):
        count += bTree[arg-1]
        arg -= arg & (-arg)
    return count


maxValue = 10000000
T = int(input())
for _ in range(T):
    input()
    n = int(input())
    bTree = [0]*maxValue
    counter = 0
    for i in range(n):
        value = int(input())
        counter += i - countLessAndEq(value)
        while(value <= maxValue):
            bTree[value-1] += 1
            value += value & (-value)
    print(counter)
