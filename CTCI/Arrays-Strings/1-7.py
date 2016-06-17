def matrix_rc_zero(matrix):
    rows = set()
    cols = set()

    for col in xrange(len(matrix)):
        for row in xrange(len(matrix[0])):
            if matrix[col][row] == 0:
                rows.add(row)
                cols.add(col)

    for col in xrange(len(matrix)):
        for row in xrange(len(matrix[0])):
            if row in rows or col in cols:
                matrix[col][row] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]

print matrix
matrix_rc_zero(matrix)
print matrix
