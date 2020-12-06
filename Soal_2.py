list_awal = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

def puter_kiri(matrix):
    hasil = []
    for i in range(len(matrix[0]), 0, -1):
        hasil.append(list(map(lambda x: x[i - 1], matrix)))

    return hasil

print(puter_kiri(list_awal))
