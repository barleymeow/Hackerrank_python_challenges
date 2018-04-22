def diagonalDifference(a):
    primary_diagonal = 0
    secondary_diagonal = 0
    for i, val in enumerate(a):
        primary_diagonal += a[i][i]
        secondary_diagonal += a[i][-i-1]
    return abs(primary_diagonal - secondary_diagonal)

a = [[11, 2, 4],
[4, 5, 6],
[10, 8, -12]]
print(diagonalDifference(a))
