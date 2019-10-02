# Complete the minimumBribes function below.
def myMinimumBribes(q):
    # bribes = 0
    # more = True
    # start_index = 0
    # while more:
    #     more = False
    #     for i in range(start_index, len(q)):
    #         try:
    #             if q[i] > q[i+1]:
    #                 if q[i] - (i + 1) > 2:
    #                     bribes = "Too chaotic"
    #                     break
    #                 start_index = i - 1
    #                 q[i], q[i+1] = q[i+1], q[i]
    #                 bribes += 1
    #                 more = True
    #                 break
    #         except IndexError:
    #             more = False
    # print(q)
    # print(bribes)

    i = 0
    # for i, p in enumerate(q):
    #     if p > i + 1:
    #         bribe = p - (i + 1)
    #         if bribe > 2:
    #             print("Too chaotic")
    #             break
    #         bribes = bribes + bribe
    bribe = 0
    new_q = q[:]
    for i in range(len(q)):
        i = i + 1
        if q[i-1] != i:
            if q[i - 1] - i > 2:
                bribe = "Too chaotic"
                break
            ri = new_q.index(i) + 1
            bribe = bribe + (ri - i)
            q1 = new_q[:i - 1]
            q1.extend([new_q.pop(ri - 1)])
            new_q = q1 + new_q[i - 1:]

    print(bribe)


def minimumBribes(q):
    moves = 0
    for i, p in enumerate(q):
        if (p-1) - i > 2:
            moves = "Too chaotic"
            break
        n = max(0,p-2)
        for j in range(n, i):
            if q[j] > p:
                moves += 1
    print(moves)


if __name__ == '__main__':
    minimumBribes([2, 1, 5, 3, 4])