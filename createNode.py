
with open('eightQueen.txt', 'w') as fp:
    print("64", end="\n",file=fp)

    for i in range(64):
        if i == 63:
            print("1", end="\n",file=fp)
        else:
            print("1", end=" ",file=fp)

    for i in range(64):
        for j in range(64):
            i_x = i//8
            i_y = i%8
            j_x = j//8
            j_y = j%8
            if i_x == j_x and i_y == j_y:
                if j == 63:
                    print("0", end="\n",file=fp)
                else:
                    print("0", end=" ",file=fp)
            elif i_x == j_x or i_y == j_y:
                if j == 63:
                    print("1", end="\n",file=fp)
                else:
                    print("1", end=" ",file=fp)
            elif abs(j_x - i_x) == abs(j_y - i_y):
                if j == 63:
                    print("1", end="\n",file=fp)
                else:
                    print("1", end=" ",file=fp)
            else:
                if j == 63:
                    print("0", end="\n",file=fp)
                else:
                    print("0", end=" ",file=fp)