# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    skip_to_next = False

    for cloud_index in range(len(c)):
        if skip_to_next:
            skip_to_next = False
            continue

        try:
            if c[cloud_index + 2] == 0:
                skip_to_next = True
            else:
                skip_to_next = False
            jumps += 1
        except IndexError:
            if cloud_index != len(c) - 1:
                jumps += 1
                break

    return jumps


if __name__ == '__main__':
    result = jumpingOnClouds([0,0,0,0,0,1,0,0,1,0])
    print(result)