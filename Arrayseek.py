import numpy as np


def Array_seek(array1, target):
    row, col = array1.shape
    list_col = range(col)
    list_row = range(row-1)
    for i in range(0, row):
        for j in range(0, col):
            if target == array1[i][j]:
                return i+1, j+1
            else:
                j += 1
        i += 1


if __name__ == "__main__":
    array1 = np.array([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
    print(Array_seek(array1, 1))
