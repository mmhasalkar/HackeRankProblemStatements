# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr) - 1
    cols = len(arr[0]) - 1
    hourglass = []
    sums = []

    for i in range(1, rows):
        for j in range(1, cols):
            hourglass.extend(arr[i - 1][j - 1:j + 2])
            hourglass.extend([arr[i][j]])
            hourglass.extend(arr[i + 1][j - 1:j + 2])
            sums.append(sum(hourglass))
            hourglass = []

    return max(sums)


if __name__ == '__main__':
    result = hourglassSum([[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]])
    print(result)