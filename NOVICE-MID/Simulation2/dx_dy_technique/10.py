n, m = map(int, input().split())
nmmap = [[0] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

row, column = 0, 0
dir_num = 1
drows, dcolumns = [0, 1, 0, -1], [1, 0, -1, 0]

nmmap[row][column] = 1
for i in range(2, n * m + 1):
    drow, dcolumn = row + drows[dir_num], column + dcolumns[dir_num]

    if not in_range(drow, dcolumn) or nmmap[drow][dcolumn] != 0:
        dir_num = (dir_num + 3) % 4
    
    row, column = row + drows[dir_num], column + dcolumns[dir_num]
    nmmap[row][column] = i

for i in range(n):
    for j in range(m):
        print(nmmap[i][j], end = ' ')
    print()