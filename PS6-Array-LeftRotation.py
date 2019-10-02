def rotLeft(a, d):
    rotations = 0
    ci = 0
    ti = ci - d
    ce = a[ci]
    te = a[ti]

    while rotations <= len(a):
        if len(a) - d == d and rotations % 2 != 0 and rotations > 1:
            ci = ci + 1
            ti = ci - d
            ce = a[ci]
            te = a[ti]
        a[ti] = ce
        ce = te
        ci = ti
        if ci < 0:
            ci = len(a) + ci
        ti = ci - d
        te = a[ti]

        rotations += 1

    return a


if __name__ == '__main__':
    result = rotLeft([41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51], 10)
    print(result)