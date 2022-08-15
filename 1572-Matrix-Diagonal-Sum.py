mat = [[5]]

def diagonalSum(mat):
    n = len(mat)
    res = 0
    for i in range(n):
        res = res + mat[i][i] + mat[-(i+1)][i]
    if n % 2 == 0:
        return res
    else:
        res = res - mat[n // 2][n // 2]
        return res      

print(diagonalSum(mat))