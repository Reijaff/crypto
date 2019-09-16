array = [[1, 2, 3, 7, 4, 1],
         [4, 5, 6, 8, 5, 2],
         [7, 8, 9, 9, 6, 3],
         [3, 6, 9, 9, 8, 7],
         [2, 5, 8, 6, 5, 4],
         [1, 4, 7, 3, 2, 1]]


message44 = "hello_my_old_friend,_i_glad_to_see_u"
message44 = "d,oh__leld_tol_ofi_s_rgieeela_nmduy_"
str1 = ""
encrypted = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

SIZE = 6

key = [[4, 5, 7], [3, 2], [1, 0], [6, 8]]

grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

for rn in key[0]:
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if count == rn:
                grid[i][j] = 1
            count += 1
for rn in key[1]:
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if count == rn:
                grid[SIZE - j - 1][i] = 1
            count += 1
for rn in key[2]:
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if count == rn:
                grid[SIZE-i-1][SIZE - j - 1] = 1
            count += 1
for rn in key[3]:
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if count == rn:
                grid[j][SIZE - i - 1] = 1
            count += 1

print(key)
for i in grid:
    print(i)

val = 0
for i in range(0, SIZE):
    for j in range(0, SIZE):
        if (grid[i][j] == 1):
            encrypted[i][j] = message44[val]
            val += 1
for i in range(0, SIZE):
    for j in range(0, SIZE):
        if (grid[SIZE - j - 1][i] == 1):
            encrypted[i][j] = message44[val]
            val += 1

for i in range(0, SIZE):
    for j in range(0, SIZE):
        if (grid[SIZE - i - 1][SIZE - j - 1] == 1):
            encrypted[i][j] = message44[val]
            val += 1

for i in range(0, SIZE):
    for j in range(0, SIZE):
        if (grid[j][SIZE - i - 1] == 1):
            encrypted[i][j] = message44[val]
            val += 1

for i in encrypted:
    print(i)
    str1 += ''.join(i)
print(str1)
