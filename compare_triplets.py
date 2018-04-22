def compare_2lists(A, B):
    #
    # they wanted to add a0, a1, a2, b0, b1, b2 as arguments but that's
    # not efficient, what if you want to compare more than 3 entries in lists?
    # Write your code here.
    # assuming that Bob and Alice have the same number of entries
    #
    a_points = 0
    b_points = 0
    for i, value in enumerate(A):
        if int(A[i]) > int(B[i]):
            a_points += 1
        if int(A[i]) < int(B[i]):
            b_points += 1

    return (a_points,b_points)

A = '5 10 5'.split()
B = '4 9 10'.split()

a, b = compare_2lists(A, B)
print(str(a) + " " + str(b))
