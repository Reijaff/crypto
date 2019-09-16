import itertools

brute = list(itertools.permutations(range(0, 9), 9))


SIZE = 6
fact = 0
decrypted = ""
encrypted = "3hb7yatu_1yva_9e_hr{0z4k4rau}u_ptuu4"
encrypted2 = "d,oh__leld_tol_ofi_s_rgieeela_nmduy_"


buf1 = ["3hb7ya",
        "tu_1yv",
        "a_9e_h",
        "r{0z4k",
        "4rau}u",
        "_ptuu4"]

buf = encrypted
array = [[1, 2, 3, 7, 4, 1],
         [4, 5, 6, 8, 5, 2],
         [7, 8, 9, 9, 6, 3],
         [3, 6, 9, 9, 8, 7],
         [2, 5, 8, 6, 5, 4],
         [1, 4, 7, 3, 2, 1]]

print(buf)

for rand in brute:
    fact += 1
    decrypted = ""

    key = [[rand[0], rand[1]], [rand[2], rand[3]], [rand[4],
                                                    rand[5], rand[6]], [rand[7], rand[8]]]
    # key = [[1, 8], [4, 5], [0, 2, 6], [3, 7]]

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

    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (grid[i][j] == 1):
                decrypted += buf[i * SIZE + j]
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (grid[SIZE-j-1][i] == 1):
                decrypted += buf[i * SIZE + j]
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (grid[SIZE-i-1][SIZE - j - 1] == 1):
                decrypted += buf[i * SIZE + j]
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            if (grid[j][SIZE - i - 1] == 1):
                decrypted += buf[i * SIZE + j]
    if decrypted[0:5] == "hy19{" and decrypted[-1] == "}":

        print(decrypted)
        print("You won!")
        break
